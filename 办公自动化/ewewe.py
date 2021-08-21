#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# print(mcbShelf[1])
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(mcbShelf[sys.argv[2]])
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        print('完成')
        print(sys.argv[1])
        print(mcbShelf.get(sys.argv[1]))
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()


""""""