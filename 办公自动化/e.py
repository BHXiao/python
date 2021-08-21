#!/usr/bin/env python
# -*- coding: utf-8 -*-


##################################################
# '''
# 将文件的行变成列   列变成行
# '''

# from openpyxl import load_workbook
#
# wb = load_workbook('qingdan.xlsx')
# ws = wb.active
# # data = []
# row = ws.max_row
# column = ws.max_column
# for x in range(1, row + 1):
#     for y in range(1, column + 1):
#         # date = ws.cell(row=x,column=y).value
#         if x > y:  # 防止x行y列这块范围的数据再次倒过来
#             ws.cell(row=x, column=y).value , ws.cell(row=y,column=x).value = ws.cell(row=y,column=x).value, ws.cell(row=x, column=y).value
#         # ws.cell(row=y, column=x).value = date
# wb.save('qingdan1.xlsx')

#########################################################################
# from openpyxl import load_workbook
# # 打开窗口选择文件
# import easygui
#
# '''
# 创建邮件信息整理成能导入的文件
# '''
# open_file = easygui.fileopenbox(title='选择原始信息文件', default=r'D:\Users\5006554\Desktop\*.xlsx')
# wb = load_workbook(open_file)
# data = ['序号', '姓名（必填）', '帐号（必填）', '密码（必填）', '部门', '是否同时创建邮箱',
#          '邮箱别名', '企业通讯录中显示的邮箱地址', '关联邮件列表地址', '重新登录修改密码设置',
#          'webmail端强制开启二次登录验证', '绑定手机号码', '工号', '联系手机', '电话/分机', '传真',
#          '国籍', '证件类型', '证件号码', '有效期', '备注\n'
#         ]
# # 表的列数
# column = len(data)
# # 表的行数
# row = wb.active.max_row
# # 新加一个列表。列表推导
# temp_list = [''for d in range(column)if d >= 0]
# # 最后要写入文件的数据
# file = ''
# # 定义一个字典，为部门定值
# department = {
#     '行政部': '行政部',
#     'IT部': 'IT部',
#     '财务部': '财务部',
#     '总办': '总办',
#     '人力资源部': '人力资源部',
#     '质量法规部': '质量法规部',
#     '政府项目部': '政府项目部',
#     '销售管理部': '营销系统/商务部',
#     '国内用户服务部': '营销系统/用服部',
#     '国内销售部': '营销系统/国内销售部',
#     '国际销售部': '营销系统/International sales department',
#     '技术支持服务部': '营销系统/用服部',
#     '用户服务部': '营销系统/用服部',
#     '国际用户服务部': '营销系统/国际用户服务部',
#     '临床医学部': '研发部/临床医学部',
#     '软件测试部': '研发部/仪器研发部',
#     '整机测试部': '研发部/仪器研发部',
#     '输注及气道管理系统部': '研发部/仪器研发部',
#     '硬件开发部': '研发部/仪器研发部',
#     '可靠性技术部': '研发部/仪器研发部',
#     '软件开发部': '研发部/仪器研发部',
#     '产品需求部': '研发部/仪器研发部',
#     '设计转换部': '研发部/仪器研发部',
#     '体外诊断仪器系统部': '研发部/仪器研发部',
#     '移动互联事业部': '研发部/仪器研发部',
#     '机械开发部': '研发部/仪器研发部',
#     '产品安全部': '研发部/仪器研发部',
#     '研发三部': '研发部/研发三部',
#     '研发二部': '研发部/试剂研发部',
#     '南京研发中心': '南京研发中心;研发部/仪器研发部',
#     '生命科学-研发一部': '生命科学/生命科学研发部;生命科学',
#     '生命科学-产品管理部': '生命科学',
#     '生命科学-研发三部': '生命科学/生命科学研发部;生命科学',
#     '生命科学-质量法规部': '质量法规部;生命科学',
#     '生命科学研发三部': '生命科学/生命科学研发部;生命科学',
#     '生命科学生产部': '生命科学',
#     '生命科学质检部': '生命科学',
#     '生命科学质量法规部': '质量法规部;生命科学',
#     '生命科学研发一部': '生命科学/生命科学研发部;生命科学',
#     '生命科学产品管理部': '生命科学',
#     '采购商务部': '生产及供应链系统/采购部/采购商务部',
#     '试剂生产部': '生产及供应链系统/试剂制造部/试剂生产部',
#     # '': '',
#     # '': '',
#     # '': '',
# }
# for i in range(row):
#     if wb.active.cell(row=i + 2, column=1).value:
#         # 姓名
#         temp_list[1-1] = wb.active.cell(row=i + 2, column=1).value
#         # 账号
#         temp_list[2-1] = wb.active.cell(row=i + 2, column=8).value
#         # 密码
#         temp_list[3-1] = 'Aa123456'
#         # 定位文件中部门为空或字典中无key值的位置
#         print(i)
#         # 部门
#         temp_list[4-1] = department[wb.active.cell(row=i + 2, column=5).value]
#         # 强制启用
#         temp_list[10-1] = '强制开启'
#         # 手机号
#         temp_list[11-1] = wb.active.cell(row=i + 2, column=9).value
#         # 工号
#         temp_list[12-1] = wb.active.cell(row=i + 2, column=2).value
#         # 最后一个回车,  csv文件写入时回车会自动下一行占用第一格
#         temp_list[-1] = '\n'
#         data.extend(temp_list)
# # 列表里有数字,要先转为数字
# file = ','.join('%s' %id for id in data)
# save_file = easygui.fileopenbox(title='保存文件为', default=r'D:\Users\5006554\Desktop\*.csv')
# f = open(save_file, 'w')
# f.write(file)
# f.close()
##################################################################################################
# import copy
#
# '''
# 拷备的不同
# '''
# a = [1, 2, 3, 4, ['a', 'b']]
#
# b = a  # 赋值
# c = a[:]  # 浅拷贝
# d = copy.copy(a)  # 浅拷贝
# e = copy.deepcopy(a)  # 深拷贝
#
# a.append(5)
# a[4].append('c')
# a[1] = 5
#
# print('a=', a)
# print('b=', b)
# print('c=', c)
# print('d=', d)
# print('e=', e)
# # a= [1, 5, 3, 4, ['a', 'b', 'c'], 5]
# # b= [1, 5, 3, 4, ['a', 'b', 'c'], 5]
# # c= [1, 2, 3, 4, ['a', 'b', 'c']]
# # d= [1, 2, 3, 4, ['a', 'b', 'c']]
# # e= [1, 2, 3, 4, ['a', 'b']]
##################################################################################
# 99乘法表
# for i in range(1,10):
#     for j in range(1, i+1):
#         print('%d*%d=%2ld '%(j, i, i*j), end='')
#     print()
#####################################################################################
# import time
# for i in range(4):
#     print(str(int(time.time()))[-2:])
#     time.sleep(1)
####################################################################################
# thislist = list(("apple", "banana", "cherry"))  # 双括号（列表期望最多1个参数，得到3个）
# print(thislist)
############################################################################################
# def myFunc(e):
#   return e['year']
#
# cars = [
#   {'car': 'Porsche', 'year': 1963},
#   {'car': 'Audi', 'year': 2010},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'Volvo', 'year': 2013}
# ]
#
# cars.sort(key=myFunc)
# print(cars)
# # [{'car': 'Porsche', 'year': 1963}, {'car': 'Audi', 'year': 2010}, {'car': 'Volvo', 'year': 2013}, {'car': 'BMW', 'year': 2019}]

###############################################################################################
# def myFunc(_):
#   print(len(_))
#   return len(_)  # 元素中字母个数(括号中可以是任何非空字符)，用来代表元素
#
# cars = ['Porsche', 'Audi', 'BMW', 'Volvo']
#
# cars.sort(key=myFunc)
# print(cars)
# # 7
# # 4
# # 3
# # 5
# # ['BMW', 'Audi', 'Volvo', 'Porsche']
#############################################################################
# 匿名函数
# x = lambda a: a + 10
# print(x(7))
# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))

######################################################################################





