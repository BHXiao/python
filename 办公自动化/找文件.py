#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


for p, d, f in os.walk('D:\python'):

    for i in f:
        if i.endswith('.py'):
            print(os.path.join(p, i))
            print('.'*10)


""""""
