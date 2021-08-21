import random
import time

import pygame
from pygame.constants import *


class HeroPlane(pygame.sprite.Sprite):
    bulletss = pygame.sprite.Group()

    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        self.Player = pygame.image.load('feijidazha_images/images/life.png')
        self.rect = self.Player.get_rect()
        self.rect.topleft = [Manager.bg_size[0] / 2 - 46 / 2, 500]
        self.speed = 5
        self.window = window
        self.bullets = pygame.sprite.Group()

    def key_control(self):
        key_pressde = pygame.key.get_pressed()
        if key_pressde[K_w] or key_pressde[K_UP]:
            if 0 < self.rect.top:
                self.rect.top -= self.speed
        if key_pressde[K_s] or key_pressde[K_DOWN]:
            if self.rect.bottom < Manager.bg_size[1]:
                self.rect.bottom += self.speed
        if key_pressde[K_a] or key_pressde[K_RIGHT]:
            if self.rect.left > 0:
                self.rect.left -= self.speed
        if key_pressde[K_d] or key_pressde[K_LEFT]:
            if self.rect.right < Manager.bg_size[0]:
                self.rect.right += self.speed
        if key_pressde[K_SPACE]:
            bullet = Bullet(self.window, self.rect.left, self.rect.top)
            self.bullets.add(bullet)
            HeroPlane.bulletss.add(bullet)

    def display(self):
        self.window.blit(self.Player, self.rect)
        self.bullets.update()
        self.bullets.draw(self.window)

    def update(self):
        self.key_control()
        self.display()

    @classmethod
    def clear_bullets(cls):
        cls.bulletss.empty()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("feijidazha_images/images/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 46 / 2 - 2, y - 11]
        self.window = screen
        self.speed = 20

    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < -11:
            self.kill()


class EnemyPlane(pygame.sprite.Sprite):
    enemy_bullet = pygame.sprite.Group()

    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        self.enemy = pygame.image.load("feijidazha_images/images/enemy1.png")
        self.rect = self.enemy.get_rect()
        x = random.randrange(1, Manager.bg_size[0], 57)
        self.rect.topleft = [x, 0]

        self.speed = 4

        self.window = window
        self.bullets = pygame.sprite.Group()
        self.direction = 'right'

    def display(self):
        self.window.blit(self.enemy, self.rect)
        self.bullets.update()  # UPdate 是精灵中的一个挂勾  调用的还是对应精灵类中的UPdate方法
        self.bullets.draw(self.window)

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right += self.speed
        elif self.direction == 'left':
            self.rect.left -= self.speed
        if self.rect.right > (Manager.bg_size[0]):
            self.direction = 'left'
        elif self.rect.left < 0:
            self.direction = 'right'
        self.rect.bottom += self.speed

    def auto_fire(self):
        num = random.randint(0, 20)
        if num == 8:
            bullet = EnemyBullet(self.window, self.rect.left, self.rect.top)
            self.bullets.add(bullet)
            EnemyPlane.enemy_bullet.add(bullet)

    def update(self):

        self.auto_move()
        self.auto_fire()
        self.display()

    @classmethod
    def clear_bullets(cls):
        cls.enemy_bullet.empty()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, window, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("feijidazha_images/images/bullet2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 58 / 2 - 2, y + 43]
        self.window = window
        self.speed = 20

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > Manager.bg_size[1]:
            self.kill()


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("D:\KwDownload\song\李玉刚-刚好遇见你.flac")
        pygame.mixer.music.set_volume(0.5)
        self.__bomb = pygame.mixer.Sound('sound/enemy1_down.wav')

    def play_background_music(self):
        pygame.mixer.music.play(-1)

    def playBombSound(self):
        pygame.mixer.Sound.play(self.__bomb)


class Bomb(object):
    def __init__(self, window, type1):
        self.screen = window
        if type1 == "enemy":
            self.image1 = [pygame.image.load
                           ("./feijidazha_images/images/enemy1_down" + str(v) + ".png") for v in range(1, 5)]
        else:
            self.image1 = [pygame.image.load
                           ("./feijidazha_images/images/me_destroy_" + str(v) + ".png") for v in range(1, 4)]
        self.index = 0
        self.bomb_coordinate = [0, 0]
        self.Visible = False

    def coordinate(self, rect):
        self.bomb_coordinate[0] = rect.left
        self.bomb_coordinate[1] = rect.top
        self.Visible = True

    def trigger(self):
        if not self.Visible:
            return
        self.screen.blit(self.image1[self.index], (self.bomb_coordinate[0], self.bomb_coordinate[1]))
        self.index += 1
        if self.index >= len(self.image1):
            self.index = 0
            self.Visible = False


class GameBackground(object):
    def __init__(self, window):
        self.image1 = pygame.image.load('feijidazha_images/images/background.png')
        self.image2 = pygame.image.load('feijidazha_images/images/background.png')
        self.window = window
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
    create_enemy_id = 30
    game_over_id = 11
    is_game_over = False
    over_time = 13

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(Manager.bg_size, 0, 32)
        self.map = GameBackground(self.window)
        self.players = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.player_bomb = Bomb(self.window, 'player')
        self.enemy_bomb = Bomb(self.window, 'enemy')
        self.sound = GameSound()

    def exit(self):
        pygame.quit()
        exit()

    def show_over_text(self):
        self.drawText('gameover %d' % Manager.over_time, 100, Manager.bg_size[1] / 2,
                      textheight=50, fontcolor=[255, 0, 0])

    def game_over_time(self):
        self.show_over_text()
        Manager.over_time -= 1
        if Manager.over_time == 0:
            pygame.time.set_timer(Manager.game_over_id, 0)
            Manager.over_time = 13
            Manager.is_game_over = False
            self.start_game()

    def start_game(self):

        HeroPlane.clear_bullets()
        print('清除玩家子弹')
        EnemyPlane.clear_bullets()
        print('清除敌机子弹')
        HeroPlane.clear_bullets()
        print('清除玩家子弹')
        # manager = Manager()
        # manager.main()
        main = Manager()  # main 主程序中定议了 系统提示下
        main.main()

    def new_player(self):
        player = HeroPlane(self.window)
        self.players.add(player)

    def new_enemy(self):
        enemy = EnemyPlane(self.window)
        self.enemys.add(enemy)

    def drawText(self, text, x, y, textheight=30, fontcolor=(255, 0, 0), backgroudcolor=None):
        font_obj = pygame.font.Font('feijidazha_images/FZY3JW.TTF', textheight)
        text_obj = font_obj.render(text, True, fontcolor, backgroudcolor)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.window.blit(text_obj, text_rect)

    def main(self):
        self.sound.play_background_music()
        self.new_player()
        pygame.time.set_timer(Manager.create_enemy_id, 1000)
        while True:
            self.map.draw()
            self.map.move()
            self.drawText('8888', 0, 0)
            if Manager.is_game_over:
                self.show_over_text()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
                elif event.type == Manager.create_enemy_id:
                    self.new_enemy()
                elif event.type == Manager.game_over_id:
                    self.game_over_time()
            self.player_bomb.trigger()
            self.enemy_bomb.trigger()
            if self.players.sprites():
                isover = pygame.sprite.spritecollide(self.players.sprites()[0], EnemyPlane.enemy_bullet, True)
                if isover:
                    Manager.is_game_over = True
                    pygame.time.set_timer(Manager.game_over_id, 1000)
                    self.player_bomb.coordinate(self.players.sprites()[0].rect)
                    self.players.remove(self.players.sprites()[0])
                    self.sound.playBombSound()
            iscollide = pygame.sprite.groupcollide(self.players, self.enemys, True, True)
            if iscollide:
                Manager.is_game_over = True  # 标志游戏线束
                pygame.time.set_timer(Manager.game_over_id, 1000)  # 开启倒计时
                items = list(iscollide.items())[0]
                print(items)
                x = items[0]
                y = items[1][0]
                self.player_bomb.coordinate(x.rect)
                self.enemy_bomb.coordinate(y.rect)
                self.sound.playBombSound()
            is_enemy = pygame.sprite.groupcollide(HeroPlane.bulletss, self.enemys, True, True)
            if is_enemy:
                items = list(is_enemy.items())[0]
                y = items[1][0]
                self.enemy_bomb.coordinate(y.rect)
                self.sound.playBombSound()
            self.players.update()
            self.enemys.update()
            pygame.display.update()
            time.sleep(0.02)


if __name__ == '__main__':
    main = Manager()
    main.main()
