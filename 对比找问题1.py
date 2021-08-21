#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import pygame
from pygame.constants import *


class HeroPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('feijidazha_images/images/life.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [480 / 2 - 46 / 2, 500]
        self.speed = 5
        self.screen = screen
        self.bullets = pygame.sprite.Group()

    def key_control(self):
        key_pressde = pygame.key.get_pressed()
        if key_pressde[K_w] or key_pressde[K_UP]:
            if 0 < self.rect.top:
                self.rect.top -= self.speed
        if key_pressde[K_s] or key_pressde[K_DOWN]:
            if self.rect.bottom < 700:
                self.rect.bottom += self.speed
        if key_pressde[K_a] or key_pressde[K_RIGHT]:
            if self.rect.left > 0:
                self.rect.left -= self.speed
        if key_pressde[K_d] or key_pressde[K_LEFT]:
            if self.rect.right < 480:
                self.rect.right += self.speed
        if key_pressde[K_SPACE]:
            bullet = Bullet(self.screen, self.rect.left, self.rect.top)
            self.bullets.add(bullet)

    def update(self):
        self.key_control()
        self.display()

    def display(self):
        self.screen.blit(self.image, self.rect)
        self.bullets.update()
        self.bullets.draw(self.screen)


class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("feijidazha_images/images/enemy1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]
        self.speed = 4
        self.screen = screen
        self.bullets = pygame.sprite.Group()
        self.direction = 'right'

    def display(self):
        self.screen.blit(self.image, self.rect)
        self.bullets.update()
        self.bullets.draw(self.screen)

    def update(self):
        self.auto_move()
        self.auto_fire()
        self.display()

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right += self.speed
        elif self.direction == 'left':
            self.rect.right -= self.speed
        if self.rect.right > 480:
            self.direction = 'left'
        elif self.rect.right < 57:
            self.direction = 'right'

    def auto_fire(self):
        random_num = random.randint(0, 20)
        if random_num == 8:
            bullet = EnemyBullet(self.screen, self.rect.left, self.rect.top)
            self.bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("feijidazha_images/images/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 46 / 2 - 2, y - 11]
        self.screen = screen
        self.speed = 20

    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < -11:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("feijidazha_images/images/bullet2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 58 / 2 - 2, y + 43]
        self.screen = screen
        self.speed = 20

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > 700-11:
            self.kill()


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('sound/game_music.wave')
        pygame.mixer.music.set_volume(0.5)

    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)


def main():
    sound = GameSound()
    sound.playBackgroundMusic()
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load('feijidazha_images/images/background.png')
    player = HeroPlane(screen)
    enemyplane = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        player.key_control()
        player.display()
        enemyplane.display()
        enemyplane.auto_move()
        enemyplane.auto_fire()
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
