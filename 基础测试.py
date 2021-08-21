#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1. 定义类


class Washer():
    def wash(self):
        print('我会洗⾐衣服')
        # <__main__.Washer object at 0x0000024BA2B34240>
        print(self)


# 2. 创建对象
haier1 = Washer()
# <__main__.Washer object at 0x0000018B7B224240>
print(haier1)
# haier1对象调⽤用实例例⽅方法
haier1.wash()
# 我会洗⾐衣服
# <__main__.Washer object at 0x0000024BA2B34240>
haier2 = Washer()
# <__main__.Washer object at 0x0000022005857EF0>
print(haier2)
