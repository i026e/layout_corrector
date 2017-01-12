#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import layout_corrector.config as config
from pynput.keyboard import Key, KeyCode

from threading import Lock

def get_key(code):
    if len(code) == 1:
        return KeyCode.from_char(code)
    elif code in Key.__dict__:
        return Key.__dict__.get(code)
             
class StateMachine:
    def __init__(self):
        self.combo = dict((key, False) for key in config.hot_keys)        
        self.num_keys_pressed = 0
        
        self.other_keys_pressed = set() 
        
        self.lock = Lock()
        
    def press(self, key):
        with self.lock:
            if (key in self.combo) and (not self.combo[key]):
                self.combo[key] = True
                self.num_keys_pressed += 1
                
            elif (key not in self.combo):
                self.other_keys_pressed.add(key)
    
    def release(self, key):
        with self.lock:
            if (key in self.combo) and (self.combo[key]):
                self.combo[key] = False
                self.num_keys_pressed -= 1
                
            elif (key not in self.combo):
                self.other_keys_pressed.discard(key)
    
    def bingo(self):        
        print(self.combo, self.other_keys_pressed)
        return len(self.combo) == self.num_keys_pressed #and \
        #        len(self.other_keys_pressed) == 0
        
    def pressed_keys(self):        
        for key, is_pressed in self.combo.items():
            if is_pressed:
                yield key
                
        while self.other_keys_pressed: #will be cleared
            yield self.other_keys_pressed.pop()

        
    

        