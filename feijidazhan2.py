#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import pygame
from pygame.constants import *
#  这个软件不理解为什么要在第一条后。原因写成了from pygame import *
#  玩家飞机类


class HeroPlanc(pygame.sprite.Sprite):
    # self是内部变量。这个可以给外部调用
    # 存放玩家子弹的组
    bulletss = pygame.sprite.Group()

    # 类属性
    def __init__(self, window):
        #  第一个参数包含第二个参数self.第一个带两个.....init  不是int
        # 精灵的初始方法，必须调用
        pygame.sprite.Sprite.__init__(self)
        # self.windowsize = windowsize  等号前后相同
        # self.PlayerSize #些条代码无效  # self.PlayerSize = (46, 57)   #  与self定义的区别：可不可以被外面识别
        # 2、创建一个玩家飞机图片。
        self.Player = pygame.image.load('feijidazha_images/images/life.png')
        #
        self.rect = self.Player.get_rect()
        # self.x = windowsize[0] / 2 - self.PlayerSize[0] / 2    #  与self定义的区别：可不可以被外面识别
        self.rect.topleft = [Manager.bg_size[0] / 2 - 46 / 2, 500]
        # # 上前的参数是通过Main（）中HeroPlanc.PlayerSize = (46, 57)传入。
        # self. y = 500
        # 移动速度
        self.speed = 5
        #  记录当前窗口对象（实例）
        self.window = window
        self.bullets = pygame.sprite.Group()
        # self.bullets = []    装精灵的列表

    # 类方法
    def key_control(self):
        key_pressde = pygame.key.get_pressed()
        if key_pressde[K_w] or key_pressde[K_UP]:
            if 0 < self. rect.top:
                self.  rect.top -= self.speed
        if key_pressde[K_s] or key_pressde[K_DOWN]:
            if self.  rect.bottom < Manager.bg_size[1]:
                self. rect.bottom += self.speed
        if key_pressde[K_a] or key_pressde[K_RIGHT]:
            if self.rect.left > 0:
                self.rect.left -= self.speed
        if key_pressde[K_d] or key_pressde[K_LEFT]:
            if self.rect.right < Manager.bg_size[0]:
                self.rect.right += self.speed
        # for event in pygame.event.get():   怎么实现 按下空格发一枚子弹？？？？？
        #     if event.type == K_SPACE:
        if key_pressde[K_SPACE]:
            # 按下空格发射子弹，导入子弹类。(实例)
            bullet = Bullet(self.window, self.rect.left, self.rect.top)
            #  当按下空格时加载玩家子弹
            # 把子弹放到列表里:加在列表尾。
            self.bullets.add(bullet)
            # self.bullets.append(bullet)
            HeroPlanc.bulletss.add(bullet)

    def display(self):
        #  3、将玩家飞机图片贴到窗口中
        # self.window.blit(self.Player, (self.x, self.y))
        self.window.blit(self.Player, self.rect)
        # 更新子弹坐标    #  #  遍历所有子弹。
        #  pygame.sprite.Group()的update方法  # for bullet in self.bullets:
        self.bullets.update()  # UPdate 是精灵中的一个挂勾  调用的还是对应精灵类中的UPdate方法
        # 把所有子弹添加到屏幕   #         #  修改子弹的Y座标
        #         bullet.auto_move()
        self.bullets.draw(self.window)
        #           子弹显示在窗口
        #         bullet.display()

    def update(self):
        self.key_control()
        self.display()

    @classmethod
    def clear_bullets(cls):
        # 清空子弹
        cls.bulletss.empty()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, window, x, y):
        pygame.sprite.Sprite.__init__(self)

        # 坐标
        # self.x = x + 46 / 2 - 2
        # self.y = y - 11
        # 实例图片  self.image为精灵类中定议变量，不能改：原因： bullet = Bullet(self.window, self.rect.left, self.rect.right)
        # self.bullets.add(bullet)  self.bullets = pygame.sprite.Group()
        self.image = pygame.image.load("feijidazha_images/images/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 46 / 2 - 2, y - 11]
        #  实例窗口
        self.window = window
        # 速度
        self.speed = 20

    def update(self):   # def display(self):
        # 修改子弹坐标 #     """显示在窗口"""
        #     self.window.blit(self.bulletimage,self.rect)
        self.rect.top -= self.speed
        # 移出空口则销毁子弹对象# def auto_move(self):
        #     self.rect.bottom -= self.speed
        if self.rect.top < -11:
            self.kill()


class EnemyPlane(pygame.sprite.Sprite):

    enemy_bullet = pygame.sprite.Group()
    # 类属性

    def __init__(self, window):  # 第一个参数包含第二个参数self.第一个带两个.2、代入的参数不实例，后面的方法调用不到
        # .....3、init  不是int
        pygame.sprite.Sprite.__init__(self)
        # self.windowsize = windowsize
        # self.PlayerSize #些条代码无效  # self.PlayerSize = (46, 57)   #  与self定义的区别：可不可以被外面识别
        # 2、创建敌机图片。
        self.enemy = pygame.image.load("feijidazha_images/images/enemy1.png")
        self.rect = self.enemy.get_rect()   # self.x = random.randint(0, windowsize[0]-57)  # 与self定义的区别：可不可以被外面识别
        x = random.randrange(1, Manager.bg_size[0], 57)
        # self.rect.topleft = [random.randint(0, Manager.bg_size[0]-57), 0]
        self.rect.topleft = [x, 0]

        # # 上前的参数是通过Main（）中HeroPlanc.PlayerSize = (46, 57)传入。
        # self.y = 0
        # 移动速度
        self.speed = 4
        #  记录当前窗口对象（实例）
        self.window = window
        self.bullets = pygame.sprite.Group()
        #   self.bullets = []
        self.direction = 'right'

    def display(self):
        #  3、将敌机图片贴到窗口中
        self.window.blit(self.enemy, self.rect)

        self.bullets.update()    # #  遍历所有子弹。（更新精灵坐标）
        self.bullets.draw(self.window)
    #   for enemybulet in self.bullets:
    #     #  修改子弹的Y座标
    #     enemybulet.auto_move()
    #     #  子弹显示在窗口
    #     enemybulet.display()

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right += self.speed
        elif self.direction == 'left':
            self.rect.left -= self.speed
        if self.rect.right > (Manager.bg_size[0]):
            self.direction = 'left'
        elif self.rect.left < 0:
            self.direction = 'right'
        # 向下移动力
        self.rect.bottom += self.speed

    def auto_fire(self):
        """自动开火 创建子弹对象 添加进列表"""
        num = random.randint(0, 20)
        if num == 8:
            bullet = EnemyBullet(self.window, self.rect.left, self.rect.top)
            # 在些导入子弹类，并传入  x  y
            self.bullets.add(bullet)
            # self.bullets.append(bullet)   # 放入列表给敌机调用
            EnemyPlane.enemy_bullet.add(bullet)

    def update(self):

        self.auto_move()
        self.auto_fire()
        self.display()

    @classmethod
    def clear_bullets(cls):
        # 清空子弹
        cls.enemy_bullet.empty()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, window, x, y):
        pygame.sprite.Sprite.__init__(self)

        # 坐标
        # self.x = x + 58 / 2 - 2
        # self.y = y + 43
        # 实例图片
        self.image = pygame.image.load("feijidazha_images/images/bullet2.png")
        self.rect = self.image.get_rect()
        # 起始位置，结束位置，步长
        # x = random.randrange(1, Manager.bg_size[0], 58)
        #　self.rect.topleft = [x + 58 / 2 - 2, y + 43]
        self.rect.topleft = [x + 58 / 2 - 2, y + 43]
        #  实例窗口
        self.window = window
        # 速度
        self.speed = 20

    def update(self):   # def display(self):
        # 修改子弹坐标 #     """显示在窗口"""
        self.rect.top += self.speed  # self.window.blit(self.bulletimage,self.rect)
        # 移出空口则销毁子弹对象# def auto_move(self):
        if self.rect.top > Manager.bg_size[1]:  # self.rect.bottom -= self.speed
            self.kill()
        #     """显示在窗口"""
        #     self.window.blit(self.bulletimage,(self.x, self.y))
        # def auto_move(self):
        #     self.y += self.speed


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()
        #  音乐模块初始化
        pygame.mixer.music.load("D:\KwDownload\song\李玉刚-刚好遇见你.flac")
        pygame.mixer.music.set_volume(0.5)
        #  声音大小   一半
        self.__bomb = pygame.mixer.Sound('sound/enemy1_down.wav')

    def play_background_music(self):
        pygame.mixer.music.play(-1)

    def playBombSound(self):
         pygame.mixer.Sound.play(self.__bomb)
        #  循环播放   播放次数
        #  上面冒号后不加东西，会将下行有用代码认为要缩进。。。


class Bomb(object):
    def __init__(self, window, type1):
        self.screen = window
        if type1 == "enemy":
            # 加载爆炸资源
            self.image1 = [pygame.image.load
                           ("./feijidazha_images/images/enemy1_down" + str(v) + ".png")for v in range(1, 5)]
        else:
            self.image1 = [pygame.image.load
                           ("./feijidazha_images/images/me_destroy_" + str(v) + ".png")for v in range(1, 5)]
        # 下标
        self.index = 0
        # 爆炸坐标
        self.bomb_coordinate = [0, 0]
        # 用于判断是否爆炸
        self.Visible = False

    def coordinate(self, rect):
        """确认坐标——引爆"""
        self.bomb_coordinate[0] = rect.left
        self.bomb_coordinate[1] = rect.top
        self.Visible = True

    def trigger(self):
        if not self.Visible:
            return
        self.screen.blit(self.image1[self.index], (self.bomb_coordinate[0], self.bomb_coordinate[1]))
        self.index += 1
        if self.index >= len(self.image1):
            # 如果下标已经到最后了 代表爆炸结束
            # 下标位置重置 mVisible重置
            self.index = 0
            self.Visible = False


class GameBackground(object):
    def __init__(self, window):
        self.image1 = pygame.image.load('feijidazha_images/images/background.png')
        self.image2 = pygame.image.load('feijidazha_images/images/background.png')
        # 窗口
        self.window = window
        # 两个y轴坐标变量
        self.y = 0
        self.y1 = -Manager.bg_size[1]
        self.speed = 6

    def draw(self):
        self.window.blit(self.image1, (0, self.y))
        self.window.blit(self.image1, (0, self.y1))

    def move(self):
        self.y += self.speed
        self.y1 += self.speed
        if self.y >= Manager.bg_size[1]:
            self.y = 0
        if self.y1 > 0:
            self.y1 = -Manager.bg_size[1]


class Manager(object):
    bg_size = (480, 700)
    # 创建敌机定时器的id  1-32  （事件）
    create_enemy_id = 30
    # 游戏结束  倒计时的ID  1-32
    game_over_id = 11
    # 游戏是否结束
    is_game_over = False
    # 倒计时时长
    over_time = 3
    # main 面向对象

    def __init__(self):
        # init 初始化    文字部分报错pygame.error: font not initialized
        pygame.init()
        # 创建窗口
        self.window = pygame.display.set_mode(Manager.bg_size, 0, 32)
        # 创建背景图片
        self.map = GameBackground(self.window)
        # self.background = pygame.image.load('feijidazha_images/images/background.png')
        # 初始化一个装玩家精灵的group
        self.players = pygame.sprite.Group()
        # 初始化一个装敌机精灵的group
        self.enemys = pygame.sprite.Group()
        # 初始化一个玩家爆炸的对象
        self.player_bomb = Bomb(self.window, 'player')
        # 初始化一个敌机爆炸的对象
        self.enemy_bomb = Bomb(self.window, 'enemy')
        # 初始化一个声音播放的对象
        self.sound = GameSound()

    def exit(self):
        # 完全退出游戏。
        # print('退出')
        pygame.quit()
        exit()

    def show_over_text(self):
        # 显示的文字  坐标  大小   颜色
        self.drawText('gameover %d' % Manager.over_time, 100, Manager.bg_size[1]/2,
                      textheight=50, fontcolor=[255, 0, 0])

    def game_over_time(self):
        self.show_over_text()
        # 倒计时-1
        Manager.over_time -= 1
        if Manager.over_time == 0:
            # 参数2改为0 定时停止
            pygame.time.set_timer(Manager.game_over_id, 0)
            # 倒计时重新开始
            Manager.over_time = 3
            Manager.is_game_over = False
            self.start_game()


    def start_game(self):
        # 重新开始游戏  有些类清空   子弹不应该在这才清除  应该在目标摧毁后立刻清空
        EnemyPlane.clear_bullets()
        HeroPlanc.clear_bullets()
        manager = Manager()
        manager.main()

    def new_player(self):
        # 创建飞机对象 添加到玩家的组
        player = HeroPlanc(self.window)
        self.players.add(player)

    def new_enemy(self):
        # 创建敌机的对象 添加到敌机的组
        enemy = EnemyPlane(self.window)
        self.enemys.add(enemy)

    # 绘制文字
    def drawText(self, text, x, y, textheight=30, fontcolor=(255, 0, 0), backgroudcolor=None):
        # 通过字体文件获取字体对象pygame.font.Font
        # font_obj = pygame.font.Font('feijidazha_images/dVM8CM_iconcool.TTF', textheight) # 字体不可用  报没有宽度
        font_obj = pygame.font.Font('feijidazha_images/FZY3JW.TTF', textheight)
        # 文字对象
        text_obj = font_obj.render(text, True, fontcolor, backgroudcolor)
        # 获取显示对象的矩形
        text_rect = text_obj.get_rect()
        # 设置显示位置坐标
        text_rect.topleft = (x, y)
        # 将文字显示到窗口上
        self.window.blit(text_obj, text_rect)

    def main(self):
        # 播放背景音乐
        self.sound.play_background_music()
        # 创建一个玩家
        self.new_player()
        # 创建一个敌机
        # self.new_enemy()
        # 开启创建敌机的定时器
        pygame.time.set_timer(Manager.create_enemy_id, 1000)
        while True:
            # 把背景图片贴到窗口
            # self.window.blit(self.map, (0, 0))
            self.map.draw()
            self.map.move()
            # 显示成绩
            self.drawText('8888', 0, 0)
            if Manager.is_game_over:
                # 判断游戏结束才显示结束文字
                self.show_over_text()
            # 遍历所有的事件
            for event in pygame.event.get():
                # 判断事件类型如果是pygame的退出
                if event.type == QUIT:
                    self.exit()
                elif event.type == Manager.create_enemy_id:
                    #  创建一个敌机
                    self.new_enemy()
                elif event.type == Manager.game_over_id:
                    # 倒计时触发的事件
                    self.game_over_time()

            # 调用爆炸的对象(触发条件)
            self.player_bomb.trigger()
            self.enemy_bomb.trigger()
            # 玩家飞机与敌机子弹的碰撞
            if self.players.sprites():
                # spritecollide而非groupcollide是因为是精灵与精灵组的碰撞
                isover = pygame.sprite.spritecollide(self.players.sprites()[0], EnemyPlane.enemy_bullet, True)
                if isover:
                    # 表示游戏结束
                    Manager.is_game_over = True
                    # 开始结束倒计时  1000毫秒=1秒
                    pygame.time.set_timer(Manager.game_over_id, 1000)
                    # 显示爆炸效果
                    self.player_bomb.coordinate(self.players.sprites()[0].rect)
                    # HeroPlanc.clear_bullets()
                    # 把玩家飞机从精灵组中移除
                    self.players.remove(self.players.sprites()[0])
                    self.sound.playBombSound()


            # 判断玩家与敌机碰撞
            iscollide = pygame.sprite.groupcollide(self.players, self.enemys, True, True)
            # 传回一个字典(玩家：xxx, 敌机：xxx)
            if iscollide:
                Manager.is_game_over = True  # 标志游戏线束
                pygame.time.set_timer(Manager.game_over_id, 1000)  # 开启倒计时
                # 获取items放入列表中
                items = list(iscollide.items())[0]
                print(items)
                x = items[0]
                y = items[1][0]
                # 玩家爆炸图片
                self.player_bomb.coordinate(x.rect)
                # 敌机爆炸图片
                self.enemy_bomb.coordinate(y.rect)
                # HeroPlanc.clear_bullets()  # 我改的
                # 爆炸的声音
                self.sound.playBombSound()
            # 玩家子弹与敌机碰撞
            is_enemy = pygame.sprite.groupcollide(HeroPlanc.bulletss, self.enemys, True, True)
            if is_enemy:
                items = list(is_enemy.items())[0]
                y = items[1][0]
                self.enemy_bomb.coordinate(y.rect)
                # EnemyPlane.clear_bullets()
                self.sound.playBombSound()

            # 玩家飞机和子弹的显示
            self.players.update()
            # 敌机和子弹的显示
            self.enemys.update()
            # self.drawText('8888', 0, 0)
            # 刷新窗口内容
            pygame.display.update()
            time.sleep(0.02)
# def main():    main 面向进程
#     """完成整个程序控制"""
#     sound = GameSound()
#     sound.play_background_music()
#     # 1、创建一个窗口
#     # windowsize = (480, 700)
#     window = pygame.display.set_mode((480, 700), 0, 32)
#     # 2、创建一个图片，当作背景
#     background = pygame.image.load('feijidazha_images/images/background.png')
#     HeroPlanc.PlayerSize = (46, 57)
#     # 外部定义属性，不建议这么做。#  与self定义的区别：可不可以被外面识别
#     player = HeroPlanc(window)
#     enemy = EnemyPlane(window)
#
#     while True:
#     # 3、将背景图片贴到窗口中
#         window.blit(background, (0, 0))  # 窗口。传入。非图片传入
#
#         # 获取事情
#         for event in pygame.event.get():
#             # 判断事件类型
#             if event.type == QUIT:
#                 # 执行pygame退出
#                 pygame.quit()
#                 # python程序退出,没有报错video system not initialized：视频系统未初始化
#                 exit()
#             # if event.type == K_SPACE:
#                 # elif event.type == KEYDOWN :
#                 #     # 检验按键是否是a或者left    只能执行一次
#                 #     if event.key == K_a or event.key == K_LEFT:
#                 #     elif event.key == K_d or event.key == K_RIGHT:
#                 #     elif event.key == K_w or event.key == K_UP:
#                 #     elif event.key == K_s or event.key == K_DOWN:
#                 #     elif event.key == K_SPACE:
#         # player.update()       # # 控制事件
#         # enemy.update()
#         player.key_control()
#         # 刷新玩家飞机
#         player.display()
#
#         # 敌机移动
#         enemy.auto_move()
#         # 敌机子弹
#         enemy.auto_fire()
#         # 刷新敌机
#         enemy.display()
#         # 4、显示窗口中的内容
#         pygame.display.update()  #  更新
#         # 控制while循环运行的速度
#         time.sleep(0.01)


if __name__ == '__main__':
    # 判断是否为主动执行还是被引用，自己运行时才执行代码
    main = Manager()
    main.main()

"""
36
"""