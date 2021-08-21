#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import re
import threading
import time
import requests
from queue import Queue


# 预下载，获取m3u8文件，读出ts链接，并写入文档
def down(headers, url, base_url):
    # 当ts文件链接不完整时，需拼凑
    resp = requests.get(url, headers=headers)
    m3u8_text = resp.text
    # print(m3u8_text)
    # 按行拆分m3u8文档
    ts_queue = Queue(10000)
    lines = m3u8_text.split('\n')
    s = len(lines)
    # 找到文档中含有ts字段的行
    concatfile = 'cache/' + "s" + '.txt'
    for i, line in enumerate(lines):
        if '.ts' in line:
            if 'http' in line:
                # print("ts>>", line)
                ts_queue.put(line)
            else:
                line = base_url + line
                ts_queue.put(line)
                # print('ts>>',line)
            filename = re.search('([a-zA-Z0-9-_]+.ts)', line).group(1).strip()
            # 一定要先写文件，因为线程的下载是无序的，文件无法按照
            # 123456。。。去顺序排序，而文件中的命名也无法保证是按顺序的
            # 这会导致下载的ts文件无序，合并时，就会顺序错误，导致视频有问题。
            open(concatfile, 'a+').write("file %s\n" % filename)
            print("\r", '文件写入中', i, "/", s, end="", flush=True)
    return ts_queue, concatfile


# 线程模式，执行线程下载
def run(ts_queue, headers):
    while not ts_queue.empty():
        url = ts_queue.get()
        filename = re.search('([a-zA-Z0-9-_]+.ts)', url).group(1).strip()
        try:
            requests.packages.urllib3.disable_warnings()
            r = requests.get(url, stream=True, headers=headers, verify=False)
            with open('cache/' + filename, 'wb') as fp:
                for chunk in r.iter_content(5242):
                    if chunk:
                        fp.write(chunk)
            print("\r", '任务文件 ', filename, ' 下载成功', end="", flush=True)
        except:
            print('任务文件 ', filename, ' 下载失败')
            ts_queue.put(url)


# 视频合并方法，使用ffmpeg
def merge(concatfile, name):
    try:
        path = 'cache/' + name + '.mp4'
        # command = 'ffmpeg -y -f concat -i %s -crf 18 -ar 48000 -vcodec libx264 -c:a aac -r 25 -g 25 -keyint_min 25 -strict -2 %s' % (concatfile, path)
        command = 'ffmpeg -y -f concat -i %s -bsf:a aac_adtstoasc -c copy %s' % (concatfile, path)
        os.system(command)
        print('视频合并完成')
    except:
        print('合并失败')


def remove():
    dir = 'cache/'
    for line in open('cache/s.txt'):
        line = re.search('file (.*?ts)', line).group(1).strip()
        # print(line)
        os.remove(dir + line)
    print("ts文件全部删除")
    try:
        os.remove('cache/s.txt')
        print('文件删除成功')
    except:
        print('文件删除失败')


if __name__ == '__main__':
    name = input('请输入视频名称：')
    url = input('请输入视频链接：').strip()
    # 测试用链接：https://yiyi.55zuiday.com/ppvod/70B5A6E3A150A99882E28EC793CAF519.m3u8
    # 链接电影：地球最后的夜晚
    base_url = 'https://yiyi.55zuiday.com/'
    headers = {
        'referer': 'https://yiyi.55zuiday.com/share/wVuAcJFy1tMy4t0x',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    start = datetime.datetime.now().replace(microsecond=0)
    print("文件开始写入")
    s, concatfile = down(headers, url, base_url)
    print('\n')
    print("文件写入结束")
    # 获取队列元素数量
    num = s.qsize()
    # 根据数量来开线程数，每五个元素一个线程
    # 最大开到50个
    print("下载任务开始")
    if num > 5:
        t_num = num // 5
    else:
        t_num = 1
    if t_num > 50:
        t_num = 50
    # print(s,concatfile)
    threads = []
    for i in range(t_num):
        t = threading.Thread(target=run, name='th-' + str(i), kwargs={'ts_queue': s, 'headers': headers})
        t.setDaemon(True)
        threads.append(t)
    for t in threads:
        time.sleep(0.4)
        t.start()
    for t in threads:
        t.join()
    print('\n')
    print("下载任务结束")
    end = datetime.datetime.now().replace(microsecond=0)
    print('写文件及下载耗时：' + str(end - start))
    merge(concatfile, name)
    remove()
    over = datetime.datetime.now().replace(microsecond=0)
    print('合并及删除文件耗时：' + str(over - end))
    print("所有任务结束")
    print('任务总时长：', over - start)



""""""