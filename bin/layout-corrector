#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import layout_corrector


def _get_autostart_path():
    dir_ = os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config/autostart/"))
    return os.path.join(dir_, "layout-corrector.desktop")

def _autostart():
    src_path = os.path.join(layout_corrector.config.script_path, "data/layout-corrector.desktop")

    autostart_path = _get_autostart_path()
    print("copying")
    print(src_path)
    print("to")
    print(autostart_path)
    res = os.system("cp -n {src} {dest}".format(src = src_path, dest = autostart_path))
    print("result", res)

def _noautostart():
    autostart_path = _get_autostart_path()
    if os.path.exists(autostart_path):
        print("removing", autostart_path)
        os.remove(autostart_path)

def _help():
    print("Usage : layout-corrector [option]")
    print("Options : ")
    print("help : show this message and exit")
    print("autostart : allow start on login and exit")
    print("noautostart : disable start on login and exit")

def _start():
    _help()
    layout_corrector.Switcher().run()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        param = sys.argv[1].strip().strip("-").lower()

        if param == "help" or param == "h":
            _help()

        elif param == "autostart" or param == "a":
            _autostart()

        elif param == "noautostart" or param == "na":
            _noautostart()

        exit(1)

    else:
        _start()



