#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:33:09 2017

@author: pavel
"""


from distutils.core import setup

setup(name="layout_corrector",

      version="0.2",
      description="Script to correct input in the wrong keyboard layout.",
      author="Pavel Klevakin",
      author_email="klev.paul@gmail.com",
      url="https://github.com/i026e/layout_corrector",

      packages=["layout_corrector", ],

      package_data={"layout_corrector": ["sounds/*.wav"]},

      scripts=["bin/layout-corrector"],

      data_files=[("/etc/xdg/autostart/", ["layout-corrector.desktop"])  ],

      install_requires=[ "pynput", "xkbgroup", ],

     )
