#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from pynput.keyboard import Key, KeyCode

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)


script_path = os.path.dirname(os.path.abspath( __file__ ))
log.info("Script path: %s", script_path)

"""
alt, alt_gr, alt_r, backspace, caps_lock, cmd, cmd_r,
ctrl, ctrl_r, delete, down, end, enter, esc,
f1, f2, f20, f3, f4, f5, f6, f7, f8, f9,
f10, f11, f12, f13, f14, f15, f16, f17, f18, f19,
home, insert, left, menu, num_lock, page_down, page_up,
pause, print_screen, right, scroll_lock, shift, shift_r, space, tab, up
"""

hot_keys = {Key.ctrl, '`'}

#cut_combo = (Key.ctrl, 'x')
#paste_combo = (Key.ctrl, 'v')

cut_combo = (Key.shift_r, Key.delete)
paste_combo = (Key.shift_r, Key.insert)


sounds = True
sound_keys = {Key.enter, Key.space, Key.backspace, Key.delete} # +alphanumeric

layout_0_sound = os.path.join(script_path, "./sounds/layout0_type_quiet.wav")
layout_1_sound = os.path.join(script_path, "./sounds/layout1_type_quiet.wav")
replace_sound = os.path.join(script_path, "./sounds/switch_quiet.wav")

replace_delay = 0.100 #seconds
