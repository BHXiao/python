#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame import *
import pygame
#  这个软件不理解为什么要在第一条后。
import time
import random
#  玩家飞机类
class HeroPlanc(object):
    # 类属性
    def __init__(self, Window, WindowSize):   #  第一个参数包含第二个参数self.第一个带两个.....init  不是int
        # self.WindowSize = WindowSize
        # self.PlayerSize #些条代码无效  # self.PlayerSize = (46, 57)   #  与self定义的区别：可不可以被外面识别
        # 2、创建一个玩家飞机图片。
        self.Player = pygame.image.load('feijidazha_images/images/life.png')
        self.x = WindowSize[0] / 2 - self.PlayerSize[0] / 2    #  与self定义的区别：可不可以被外面识别
        # 上前的参数是通过Main（）中HeroPlanc.PlayerSize = (46, 57)传入,不建议这样做。
        self. y = 500
        # 移动速度
        self.speed = 5
        #  记录当前窗口对象（实例）
        self.Window = Window
        self.bullets = []
    # 类方法
    def key_control(self):
        key_pressde = pygame.key.get_pressed()
        if key_pressde[K_w] or key_pressde[K_UP]:
            if 0 < self. y:
                self. y -= self.speed
        if key_pressde[K_s] or key_pressde[K_DOWN]:
            if self. y < 700-57:
                self.y += self.speed
        if key_pressde[K_a] or key_pressde[K_RIGHT]:
            if self.x > 0:
                self.x -= self.speed
        if key_pressde[K_d] or key_pressde[K_LEFT]:
            if self.x < 480-46:
                self.x += self.speed
        # for event in pygame.event.get():   怎么实现 按下空格发一枚子弹？？？？？
        #     if event.type == K_SPACE:
        if key_pressde[K_SPACE]:
            # 按下空格发射子弹，导入子弹类。(实例)
            bullet = Bullet(self.Window, self.x, self.y)   #  当按下空格时加载玩家子弹
            #把子弹放到列表里:加在列表尾。
            self.bullets.append(bullet)
    def display(self):
         #  3、将玩家飞机图片贴到窗口中
        self.Window.blit(self.Player, (self.x, self.y))
         #  遍历所有子弹。
        for bullet in self.bullets:
                #  修改子弹的Y座标
                bullet.auto_move()
                #  子弹显示在窗口
                bullet.display()
class Bullet(object):
    def __init__(self, Window, x, y):
        # 坐标
        self.x = x + 46 / 2 - 2
        self.y = y - 11
        # 实例图片
        self.bulletimage = pygame.image.load("feijidazha_images/images/bullet1.png")
        #  实例窗口
        self.Window = Window
        # 速度
        self.speed = 20
    def display(self):
        """显示在窗口"""
        self.Window.blit(self.bulletimage,(self.x, self.y))
    def auto_move(self):
        self.y -= self.speed
class EnemyPlane(object):
    # 类属性
    def __init__(self, Window, WindowSize):  # 第一个参数包含第二个参数self.第一个带两个.2、代入的参数不实例，后面的方法调用不到
        # .....3、init  不是int
        self.WindowSize = WindowSize
        # self.PlayerSize #些条代码无效  # self.PlayerSize = (46, 57)   #  与self定义的区别：可不可以被外面识别
        # 2、创建敌机图片。
        self.enemy = pygame.image.load("feijidazha_images/images/enemy1.png")
        self.x = random.randint(0, WindowSize[0]-57)  # 与self定义的区别：可不可以被外面识别
        # 上前的参数是通过Main（）中HeroPlanc.PlayerSize = (46, 57)传入。
        self.y = 0
        # 移动速度
        self.speed = 4
        #  记录当前窗口对象（实例）
        self.Window = Window
        self.bullets = []
        self.direction = 'right'

    def display(self):
        #  3、将敌机图片贴到窗口中
        self.Window.blit(self.enemy, (self.x, self.y))

        #  遍历所有子弹。
        for enemybulet in self.bullets:
            #  修改子弹的Y座标
            enemybulet.auto_move()
            #  子弹显示在窗口
            enemybulet.display()
    def auto_move(self):
        if self.direction == 'right': # and self.x < (WindowSize[0]-57):
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        if self.x > (self.WindowSize[0]-57):
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'
    def auto_fire(self):
        """自动开火 创建子弹对象 添加进列表"""
        num = random.randint(0, 20)
        if num == 8:
            bullet = EnemyBullet(self.Window, self.x, self.y)    #在些导入子弹类，并传入  x  y
            self.bullets.append(bullet)   # 放入列表给敌机调用
class EnemyBullet(object):
    def __init__(self, Window, x, y):
        # 坐标
        self.x = x + 58 / 2 - 2
        self.y = y + 43
        # 实例图片
        self.bulletimage = pygame.image.load("feijidazha_images/images/bullet2.png")
        #  实例窗口
        self.Window = Window
        # 速度
        self.speed = 20
    def display(self):
        """显示在窗口"""
        self.Window.blit(self.bulletimage,(self.x, self.y))
    def auto_move(self):
        self.y += self.speed
class GameSound(object):
    def __init__(self):
        pygame.mixer.init()  #  音乐模块初始化
        pygame.mixer.music.load("D:\KwDownload\song\李玉刚-刚好遇见你.flac")
        pygame.mixer.music.set_volume(0.5)   #  声音大小   一半
    def PlayBackgroundMusic(self):
        pygame.mixer.music.play(-1)    #  循环播放   播放次数
def main():
    """完成整个程序控制"""
    sound = GameSound()
    sound.PlayBackgroundMusic()
    # 1、创建一个窗口
    WindowSize = (480, 700)
    Window = pygame.display.set_mode(WindowSize, 0, 32)
    # 2、创建一个图片，当作背景
    Background = pygame.image.load('feijidazha_images/images/background.png')
    HeroPlanc.PlayerSize = (46, 57)   #外部定义属性，不建议这么做。#  与self定义的区别：可不可以被外面识别
    player = HeroPlanc(Window, WindowSize)
    enemy = EnemyPlane(Window, WindowSize)

    while True:
    # 3、将背景图片贴到窗口中
        Window.blit(Background, (0, 0))  # 窗口。传入。非图片传入

        # 获取事情
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序退出,没有报错video system not initialized：视频系统未初始化
                exit()
            # if event.type == K_SPACE:
                # elif event.type == KEYDOWN :
                #     # 检验按键是否是a或者left    只能执行一次
                #     if event.key == K_a or event.key == K_LEFT:
                #     elif event.key == K_d or event.key == K_RIGHT:
                #     elif event.key == K_w or event.key == K_UP:
                #     elif event.key == K_s or event.key == K_DOWN:
                #     elif event.key == K_SPACE:
        # 控制事件
        player.key_control()
        # 刷新玩家飞机
        player.display()
        # 刷新敌机
        enemy.display()
        # 敌机移动
        enemy.auto_move()
        # 敌机子弹
        enemy.auto_fire()
        # 4、显示窗口中的内容
        pygame.display.update()  #  更新
        # 控制while循环运行的速度
        time.sleep(0.01)



if __name__ == '__main__':    #判断是否为主动执行还是被引用，自己运行时才执行代码
    main()



""""36"""