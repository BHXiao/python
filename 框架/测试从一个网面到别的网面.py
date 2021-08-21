#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
# 定义一个打开谷歌浏览器的对象(浏览器驱动位置，如果在全局里就不用)
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get('https://www.taobao.com/')
driver.find_element_by_link_text('女装').click()
# driver.find_element_by_class_name("rax-image ").click()


""""""