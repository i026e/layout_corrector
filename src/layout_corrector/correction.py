#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ru_to_en = "f,dult`;pbqrkvyjghcnea[wxio]sm\'.zF<DULT~:PBQRKVYJGHCNEA{WXIO}SM\">Z"

ru_en_translation = str.maketrans(ru, ru_to_en)
en_ru_translation = str.maketrans(ru_to_en, ru)

def has_chars(s, chars_list):
    for sym in s:
        for ch in chars_list:
            if ch == sym:
                return True
    return False

def correct(bad_str):
    if has_chars(bad_str, ru):
        return bad_str.translate(ru_en_translation)        
    else:
        return bad_str.translate(en_ru_translation)  