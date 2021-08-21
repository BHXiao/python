#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame import *
import pygame
#  这个软件不理解为什么要入第一条后。
import time


def main():
    """完成整个程序控制"""
    # 1、创建一个窗口
    WindowSize = (480, 700)
    PlayerSize = (46, 57)

    Window = pygame.display.set_mode(WindowSize)
    # 2、创建一个图片，当作背景
    Background = pygame.image.load('feijidazha_images/images/background.png')
    # 2、创建一个玩家飞机图片。
    Player = pygame.image.load('feijidazha_images/images/life.png')
    x = WindowSize[0] / 2 - PlayerSize[0] / 2
    y = 500
    # 移动速度
    speed = 10
    while True:




        # 3、将背景图片贴到窗口中
        Window.blit(Background, (0, 0))  # 窗口。传入。非图片传入
        # 3、将玩家图片贴到窗口中
        Window.blit(Player, (x, y))
        # 获取事情
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序退出,没有报错video system not initialized：视频系统未初始化
                exit()
            # elif event.type == KEYDOWN :
            #     # 检验按键是否是a或者left    只能执行一次
            #     if event.key == K_a or event.key == K_LEFT:
            #     elif event.key == K_d or event.key == K_RIGHT:
            #     elif event.key == K_w or event.key == K_UP:
            #     elif event.key == K_s or event.key == K_DOWN:
            #     elif event.key == K_SPACE:
        key_pressde = pygame.key.get_pressed()
        if key_pressde[K_w] or key_pressde[K_UP]:
            if 0 < y:
                y -= speed
        if key_pressde[K_s] or key_pressde[K_DOWN]:
            if y < 700-57:
                y += speed
        if key_pressde[K_a] or key_pressde[K_RIGHT]:
            if x > 0:
                x -= speed
        if key_pressde[K_d] or key_pressde[K_LEFT]:
            if x < 480-46:
                x += speed
        if key_pressde[K_SPACE]:
            print('空格')


        # 4、显示窗口中的内容
        pygame.display.update()  #  更新

        time.sleep(0.01)


if __name__ == '__main__':    #判断是否为主动执行还是被引用，自己运行时才执行代码
    main()

