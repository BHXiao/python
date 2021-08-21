#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import zipfile

# zipF = zipfile.ZipFile(r'E:\桌面保存文件\补录验收单\补录验收单.zip', 'r')
# zipF.extractall('E:\\1')
# print(zipF.namelist())
# z = zipF.namelist()
# for i in z:
#     print(i.encode('utf-8'))
print(os.listdir('.'))
print(os.path.abspath('.'))
# print(os.path.isdir(r'e:\1\2\3.txt'))
# print(list(os.walk('e:\\1')))
# [('e:\\1', ['2', '4'], ['1.txt']), ('e:\\1\\2', ['3'], ['2.txt']), ('e:\\1\\2\\3', [], ['1结束.txt']), ('e:\\1\\4', [], ['4.txt'])]

# for folderName, subfolders, filenames in [['E:\\1',   ['2', '4'],['1.txt']],
#                                           ['E:\\1\\2',['5', '4'],['1.txt']],
#                                           ['E:\\1',   ['2', '4'],['1.txt']]
#                                           ]:
#     pass
# for folderName, subfolders, filenames in os.walk('e:\\1'):
#     print(folderName)
#     # print('----------')
#     print(subfolders)
#     # print('----------')
#     print(filenames)
#     print('----------')
    # for subfolder in subfolders:
    #     print(folderName + '\\' + subfolder)
    # for filename in filenames:
    #     print(folderName + '\\' + filename)
    # print('')
    #
