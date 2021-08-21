#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import os
import re
import threading
import time
from queue import Queue
import requests
from Crypto.Cipher import AES  # 改文件夹名Python36\Lib\site-packages


# 传入链接，完成写文件操作及获取key链接
def parse(url, headers, base_url):
    resp = requests.get(url, headers=headers)
    # 匹配key链接
    key_url = re.search('"(.*?key.key)"', resp.text).group(1).strip()
    # print(key_url)
    m3u8_text = resp.text
    # print(m3u8_text)
    # 按行拆分m3u8文档
    ts_queue = Queue(10000)
    lines = m3u8_text.split('\n')
    s = len(lines)
    # 找到文档中含有ts字段的行
    concatfile = 'cache/' + "zzz" + '.txt'
    for i, line in enumerate(lines):
        # 我找的链接里，m3u8文件里是js链接，需要替换
        if '.js' in line:
            line = re.sub('\.js', '.ts', line)
            if 'http' in line:
                # print("ts>>", line)
                ts_queue.put(line)
            filename = re.search('([a-zA-Z0-9-_]+\.ts)', line).group(1).strip()
            # 一定要先写文件，因为线程的下载是无序的，文件无法按照
            # 123456。。。去顺序排序，而文件中的命名也无法保证是按顺序的
            # 这会导致下载的ts文件无序，合并时，就会顺序错误，导致视频有问题。
            open(concatfile, 'a+').write("file %s\n" % filename)
            print("\r", '文件写入中', i, "/", s, end="", flush=True)
        else:
            if '.ts' in line:
                if 'http' in line:
                    # print("ts>>", line)
                    ts_queue.put(line)
                else:
                    line = base_url + line
                    ts_queue.put(line)
                    # print('ts>>',line)
                filename = re.search('([a-zA-Z0-9-_]+\.ts)', line).group(1).strip()
                # 一定要先写文件，因为线程的下载是无序的，文件无法按照
                # 123456。。。去顺序排序，而文件中的命名也无法保证是按顺序的
                # 这会导致下载的ts文件无序，合并时，就会顺序错误，导致视频有问题。
                open(concatfile, 'a+').write("file %s\n" % filename)
                print("\r", '文件写入中', i, "/", s, end="", flush=True)
    return ts_queue, concatfile, key_url


# 传入key链接，对key进行相关操作
def get_key(key_url):
    k = requests.get(key_url, headers=headers)
    key = k.content
    cryptor = AES.new(key, AES.MODE_CBC, key)
    return cryptor


# 下载操作
def down(ts_queue, headers, cryptor):
    while not ts_queue.empty():
        url = ts_queue.get()
        filename = re.search('([a-zA-Z0-9-_]+\.ts)', url).group(1).strip()
        try:
            requests.packages.urllib3.disable_warnings()
            resp = requests.get(url, headers=headers)
            with open('cache/' + filename, 'ab+') as f:
                data = cryptor.decrypt(resp.content)
                f.write(data)
            print("\r", '任务文件 ', filename, ' 下载成功', end="", flush=True)
        except:
            print('任务文件 ', filename, ' 下载失败')
            ts_queue.put(url)


# 合并操作
def merge(concatfile, name):
    try:
        path = 'cache/' + name + '.mp4'
        # command = 'ffmpeg -y -f concat -i %s -crf 18 -ar 48000 -vcodec libx264 -c:a aac -r 25 -g 25 -keyint_min 25 -strict -2 %s' % (concatfile, path)
        command = 'ffmpeg -y -f concat -i %s -bsf:a aac_adtstoasc -c copy %s' % (concatfile, path)
        os.system(command)
        print('视频合并完成')
    except:
        print('合并失败')


# 565 1280

# 删除操作
def remove(concatfile):
    dir = 'cache/'
    for line in open(concatfile):
        line = re.search('file (.*?\.ts)', line).group(1).strip()
        os.remove(dir + line)
    print("ts文件全部删除")
    try:
        os.remove(concatfile)
        print('文件删除成功')
    except:
        print('文件删除失败')


if __name__ == '__main__':
    name = input('请输入视频名称：')
    # 时效性链接
    url = 'https://meiju8.qfxmj.com/20191112/xVEwe432/2000kb/hls/index.m3u8?wsSecret=e16e458821a72c67fb51d57287de91e5&wsTime=1574232518&watch=ae6f4caa08e521511949081bd4dd75f9'
    headers = {
        'origin': 'https://ww4.hanjutv.com',
        'referer': 'https://m.dajueshanpiaoliu.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    start = datetime.datetime.now().replace(microsecond=0)
    print("文件开始写入")
    # 需要就写，不需要不写
    # 该网站不需要
    base_url = None
    ts_queue, concatfile, key_url = parse(url, headers, base_url)
    print('\n')
    print("文件写入结束")
    # 把key链接传给方法解析key值
    cryptor = get_key(key_url)
    # 获取队列元素数量
    num = ts_queue.qsize()
    # 根据数量来开线程数，每五个元素一个线程
    # 最大开到50个
    print("下载任务开始")
    if num > 5:
        t_num = num // 5
    else:
        t_num = 1
    if t_num > 50:
        t_num = 50
    threads = []
    for i in range(t_num):
        t = threading.Thread(target=down, name='th-' + str(i),
                             kwargs={'ts_queue': ts_queue, 'headers': headers, 'cryptor': cryptor})
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
    remove(concatfile)
    over = datetime.datetime.now().replace(microsecond=0)
    print('合并及删除文件耗时：' + str(over - end))
    print("所有任务结束")
    print('任务总时长：', over - start)


""""""