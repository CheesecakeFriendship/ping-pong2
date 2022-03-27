from pygame import *

from random import randint

class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image),(65, 65))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
#     def update(self):
#         keys = key.get_pressed()
#         if keys[K_LEFT] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys[K_RIGHT] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed
#         if keys[K_a] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys[K_d] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed
#     def fire(self):
#         keys = key.get_pressed()
#         if keys[K_SPACE]:
#             bullet = Bullet('bullet.png', self.rect.x, self.rect.top, 10)
#             bullets.add(bullet)

class Player2(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > win_height:
#             self.rect.x = randint(0, win_height - 100)
#             self.rect.y = 0
#             lost = lost + 1
        
# window = display.set_mode((700, 500))
# win_width = 700
# win_height = 500
# display.set_caption()
# background = transform.scale(image.load(""),(700, 500))
# sprite1 = Player("rocket.png", 10, 425, 5)

# font.init()
# font1 = font.SysFont('Arial', 36)
# lost = 0

# font.init()
# font = font.SysFont('Arial', 70)
# win = font.render('YOU WIN!', True, (255, 215, 0))

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))


# game = True
# finish = False
while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
    if ball.rect.y > win_height-50
        or ball.rect.y < 0:
            speed_y *= -1
        
#         sprite_list = sprite.spritecollide(sprite1, monsters, False)
#         sprite_list = sprite.spritecollide(sprite1, asteroids, True)
#         if sprite.groupcollide(monsters, bullets, True, True):
#             monsters.add(Enemy("ufo.png", randint(1, 635), 1, randint(1, 2)))

    display.update()
