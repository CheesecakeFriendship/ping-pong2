from pygame import *

from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.player_image = player_image
        self.image = transform.scale(image.load(player_image),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 50:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed


class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 600:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed



class Ball(GameSprite):
    def update(self):
        pass


player1 = Player1("ping.png", 50, 250, 10, 50, 200)
player2 = Player2("ping.png", 650, 250, 10, 50, 200)
ball = Ball("Ohmyballs.jpg", 350, 250, 1, 25, 25)


window = display.set_mode((700, 500))
background = transform.scale(image.load("place.png"),(700, 500))
win_width = 700
win_height = 500


font.init()

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSE!', True, (180, 0, 0))


speed_x = 2
speed_y = 2


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
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

        if sprite.collide_rect(player1, ball): 
            ball.rect.x = player1.rect.x + 50
            speed_x *= -1
        
        if sprite.collide_rect(player2, ball):
            ball.rect.x = player2.rect.x -50
            speed_x *= -1


    display.update()