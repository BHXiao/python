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
# import shutil


def file_exists(text):
    """当文件下载完成后关闭浏览器"""
    while True:
        if os.path.isfile(down_dir + text):
            # driver.close()
            time.sleep(0.5)
            if (down_dir + text).endswith('.key'):
                # time.sleep(2)
                # 把key链接传给方法解析key值
                key = open(down_dir + text, 'rb').read()
                cryptor1 = AES.new(key, AES.MODE_CBC, key)
                os.remove(down_dir + text)
                return cryptor1
            # if (down_dir + text).endswith('.ts'):
            #     print('开始解密' + down_dir + text)
            break

        else:
            time.sleep(0.2)
    pass


def down_url(url):
    """下载文件"""

    # print(urlurl)
    driver.get(url)
    # 下载完关闭浏览器
    fileName = url.split('/')[-1]
    return file_exists(fileName)


def get_url():
    """生成文件下载链接和本地文件链接"""
    f = open(down_dir + 'index.m3u8', 'r')
    lines = f.read().split('\n')
    for i in lines:
        if i.endswith('.ts'):
            # print(i)
            # locaFile.append(down_dir + i)
            url.append(urlPrdfix + i)
        elif re.findall('.key', i):
            r = i.split('\"')[1]
            # print(r)
            # key_file.append(down_dir + r)
            # locaFile.append(down_dir + i)
            url.append(urlPrdfix + r)
    f.close()
    os.remove(down_dir + 'index.m3u8')
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
        if i.endswith('.m3u8') or i.endswith('.ts') or i.endswith('.key'):
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

    # # https://vod4.guotejia.com/202101/b331fa2a/index.m3u8
    # 网址前缀
    urlPrdfix = re.match('.*/', url_m3u8).group(0)

    # 网络地址
    url = []
    # 本地文件保存连接
    # locaFile = []
    # key 文件地址
    # key_file = []
    # 静默方式打开
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(options=chrome_options)

    driver = webdriver.Chrome()
    driver.minimize_window()

    down_url(url_m3u8)
    # f = open(down_dir +fileName, 'r')
    get_url()
    cryptor = down_url(url[0])
    f_mp4 = open(path, 'wb')
    for i in url[1:]:
        # 下载
        down_url(i)
        #  本地解密合并操作
        if cryptor:
            print('开始解密' + down_dir + i.split('/')[-1])
            f_temp = open(down_dir + i.split('/')[-1], 'rb')
            bit = cryptor.decrypt(f_temp.read())
            print('开始吞并' + down_dir + i.split('/')[-1] + '文件')
            f_mp4.write(bit)
            f_temp.close()
            print('吞并' + down_dir + i.split('/')[-1] + '文件完成')
            os.remove(down_dir + i.split('/')[-1])
            print('删除' + down_dir + i.split('/')[-1] + '文件完成')
        else:
            print('开始吞并' + down_dir + i.split('/')[-1] + '文件')
            f_temp = open(down_dir + i.split('/')[-1], 'rb')
            f_mp4.write(f_temp.read())
            print('吞并' + down_dir + i.split('/')[-1] + '文件完成')
            os.remove(down_dir + i.split('/')[-1])
            print('删除' + down_dir + i.split('/')[-1] + '文件完成')
    driver.close()
    f_mp4.close()
    print('已生成' + path)



    # 合成MP4文件，删除.ts文件
    # merge()
    # 删除key m3u8 ts文件
    remove()
    time2 = datetime.datetime.now().replace(microsecond=0)
    print('下载用时' + str(time2 - time1))

""""""
