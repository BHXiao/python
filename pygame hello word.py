        import pygame
import sys
from pygame.locals import *

pygame.init()  # 初始化
screen = pygame.display.set_mode((800, 600), 0, 30)  # 主界面
# py = pygame.image.load("feijidazha_images/images/me1.png")
# screen.blit(py, (0, 0))

while True:  # main loop
    for event in pygame.event.get():  # 获取事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  #   报错 video system not initialized
    pygame.display.update()
