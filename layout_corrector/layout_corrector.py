#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 07:49:21 2017

@author: pavel
"""

import subprocess

from pynput.keyboard import Controller, Listener
from xkbgroup import XKeyboard

import layout_corrector.config as config
import layout_corrector.correction as correction
import layout_corrector.state as state


group_sounds = {0: config.layout_0_sound,
                1: config.layout_1_sound,}


def key_combo(keyboard, modifier, key):
    """
    with keyboard.pressed(modifier):
        keyboard.press(key)
        keyboard.release(key)
    """
    keyboard.press(modifier)
    keyboard.press(key)
    keyboard.release(key)
    keyboard.release(modifier)

def cut_to_buffer(keyboard):
    key_combo(keyboard, *config.cut_combo)

def paste_from_buffer(keyboard):
    key_combo(keyboard, *config.paste_combo)

def get_buffer():
    #pyperclip
    p = subprocess.Popen(['xsel', '-b', '-o'],
                         stdout=subprocess.PIPE, close_fds=True)
    stdout, stderr = p.communicate()
    return stdout.decode('utf-8')

def set_buffer(text):
    p = subprocess.Popen(['xsel', '-b', '-i'],
                             stdin=subprocess.PIPE, close_fds=True)
    p.communicate(input=text.encode('utf-8'))

def play(sound):
    if config.sounds:
	    try:
            p = subprocess.Popen(["aplay", sound],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, close_fds=True)
            stdout, stderr = p.communicate()
            print(stdout.decode('utf-8'))
        except Exception as e:
            print(e)

class Switcher:
    def __init__(self):
        self.xkb = XKeyboard()
        self.controller = Controller()
        self.state = state.StateMachine()

        self.busy = False

    def run(self):
        with Listener(on_press = self.on_key_press,
                      on_release = self.on_key_release) as listener:
            listener.join()


    def announce_key(self):
        group = self.xkb.group_num
        play(group_sounds.get(group))


    def on_key_press(self, key):
        print("press", key)
        self.state.press(key)

        try:
            char = key.char
            self.announce_key()
        except Exception as e:
            if key in config.sound_keys:
                self.announce_key()


    def on_key_release(self, key):
        print("release", key)
        if self.state.bingo():
            self.replace_selection()
        self.state.release(key)

    def get_text(self):
        cut_to_buffer(self.controller)

        text = get_buffer()
        print("get text", text)
        return text

    def set_text(self, text):
        print("set_text", text)
        set_buffer(text)
        paste_from_buffer(self.controller)
        set_buffer("")

    def replace_selection(self):
        if not self.busy:
            self.busy = True
            print("replacing")

            for key in self.state.pressed_keys():
                self.controller.release(key)

            text = self.get_text()

            if len(text) > 0:
                text = correction.correct(text)

                self.set_text(text)
                play(config.replace_sound)

            self.busy = False

if __name__ == '__main__':
    Switcher().run()
