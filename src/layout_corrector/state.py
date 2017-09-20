#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

import config
from pynput.keyboard import Key, KeyCode

from threading import Lock

log = logging.getLogger(__name__)

def get_key(code):
    if len(code) == 1:
        return KeyCode.from_char(code)
    elif code in Key.__dict__:
        return Key.__dict__.get(code)

def get_name(key):
    if isinstance(key, KeyCode):
        return key.char
    return key

class StateMachine:
    def __init__(self):
        self.combo = dict((key, False) for key in config.hot_keys)
        self.num_keys_pressed = 0

        self.other_keys_pressed = set()

        self.lock = Lock()

    def press(self, key):
        key_name = get_name(key)
        with self.lock:
            if (key_name in self.combo) and (not self.combo[key_name]):
                self.combo[key_name] = True
                self.num_keys_pressed += 1

            elif (key not in self.combo):
                self.other_keys_pressed.add(key)

    def release(self, key):
        key_name = get_name(key)
        with self.lock:
            if (key_name in self.combo) and (self.combo[key_name]):
                self.combo[key_name] = False
                self.num_keys_pressed -= 1

            elif (key not in self.combo):
                self.other_keys_pressed.discard(key)

    def bingo(self):
        log.debug("Shortcut keys: %s", self.combo)
        log.debug("Other keys pressed: %s", self.other_keys_pressed)

        return len(self.combo) == self.num_keys_pressed #and \
        #        len(self.other_keys_pressed) == 0

    def pressed_keys(self):
        for key, is_pressed in self.combo.items():
            if is_pressed:
                yield key

        while self.other_keys_pressed: #will be cleared
            yield self.other_keys_pressed.pop()
