#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import os
import re
# import threading
import time
# from queue import Queue
# import requests
from Crypto.Cipher import AES
from selenium import webdriver
import requests
from you_get import common as you_get


def down_url(url):
    """下载文件"""
    # print(urlurl)
    try:
        driver.get(url)
        # test = "you-get - i \"" + url + "\""
        # os.system(test)

    except:
        print('下载失败')
        pass
    # print(driver)
    # # 下载完关闭浏览器
    # fileName = url.split('/')[-1]
    # return fileName


def get_url():
    while True:
        if os.path.isfile(down_dir + 'index.m3u8'):
            """生成文件下载链接和本地文件链接"""
            time.sleep(1)
            f = open(down_dir + 'index.m3u8', 'r')
            lines = f.read().split('\n')
            for i in lines:
                if i.endswith('.image'):
                    # print(i)
                    # locaFile.append(down_dir + i)
                    url.append(i)
            f.close()
            os.remove(down_dir + 'index.m3u8')
            break

            # print(url)
            # return url


# 打开下下载的key，对key进行相关操作
# def get_key():
#     # for i in locaFile:
#     #     if re.findall('.key', i):
#


# def merge():
#
#     for i in locaFile:
#
def remove():
    deletefile = os.listdir(down_dir)
    for i in deletefile:
        if i.endswith('.m3u8') or i.endswith('.ts') or i.endswith('.key') or i.endswith('.image'):
            # f.write(open(down_path + i, 'rb').read())
            os.remove(down_dir + i)

    pass


if __name__ == '__main__':
    time1 = datetime.datetime.now().replace(microsecond=0)
    url_m3u8 = input('清输入m3u8地址：')
    # 本地存放目前
    down_dir = 'D:/Users/5006554/Downloads/'
    name = input('输入文件名：')
    path = down_dir + name + '.mp4'

    url = []

    driver = webdriver.Chrome()
    driver.minimize_window()

    down_url(url_m3u8)
    get_url()
    f_mp4 = open(path, 'wb')
    for i in url:

        # 替换~号为_号
        # t = i.split('/')[-1].replace('~', '_').replace('image', 'ts')
        t = i.split('/')[-1].replace('~', '_')

        # 下载
        down_url(i)
    #  本地解密合并操作
    #     time.sleep(1)
        while True:
            if os.path.isfile(down_dir + i.split('/')[-1].replace('~', '_')):
                # time.sleep(1)
                # os.rename(down_dir + i.split('/')[-1].replace('~', '_'), down_dir + t)
                time.sleep(0.2)
                print('开始吞并' + down_dir + t + '文件')
                f_temp = open(down_dir + t, 'rb')
                f_mp4.write(f_temp.read())
                print('吞并' + down_dir + t + '文件完成')
                f_temp.close()
                # 减少删除的时间，是否成功
                # os.remove(down_dir + t)
                # print('删除' + down_dir + t + '文件完成')
                break
    driver.close()
    f_mp4.close()
    print('已生成' + path)


    remove()
    time2 = datetime.datetime.now().replace(microsecond=0)
    print('下载用时' + str(time2 - time1))

""""""
