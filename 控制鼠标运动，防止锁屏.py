#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui
import random
import time

width, height = pyautogui.size()
try:
    while True:
        x = random.randint(0, width)
        y = random.randint(0, height)
        print(x, y)
        pyautogui.moveTo(x, y, 1)
        time.sleep(10)
except KeyboardInterrupt:  # 处理 Ctrl-C 按键
        print('\nDone.')

""""""