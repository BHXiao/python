"""
1. 弄一个窗口，让我们的这个贪吃蛇游戏展示
2. 窗口上对于我们需要的东西进行初始化：默认操作
3. 游戏动起来能够让蛇往前走
4. 接受用户操作
5. 设立规则：
"""
import pygame, sys, random    # 游戏系统随机
from pygame.locals import *

#  弄一个窗口
pygame.init()    #初始化

redColor = pygame.Color(255, 0, 0)         #  蛇的位置
blackColor = pygame.Color(0, 0, 0)         #
whiteColor = pygame.Color(255, 255, 255)   #

snakePosition = [100, 100]                 #
snakeBody = [[100, 100], [80, 100], [60, 100]] #
targetflag = 1                 #
targetPosition = [300, 300]                              #
direction = 'right'                        #
score = 0                                  #
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('贪吃蛇-你的分数： '+ str(score))
while True:
     playSurface.fill(blackColor)
     for position in snakeBody:
        pygame.draw.rect(playSurface, whiteColor, redColor, Rect)
        #没写完。。。。。
