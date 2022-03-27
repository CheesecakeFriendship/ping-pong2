from pygame import *

from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.x += self.speed

class Player2(GameSprite):
    def update(self):
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.x += self.speed
        
window = display.set_mode((700, 500))
win_width = 700
win_height = 500
# display.set_caption()
# background = transform.scale(image.load(" "),(700, 500))

font.init()

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSE!', True, (180, 0, 0))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

    display.update()