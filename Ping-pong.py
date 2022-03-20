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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            bullet = Bullet('bullet.png', self.rect.x, self.rect.top, 10)
            bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(0, win_height - 100)
            self.rect.y = 0
            lost = lost + 1

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(0, win_height - 100)
            self.rect.y = 0


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()
            self.remove(bullets)

window = display.set_mode((700, 500))
win_width = 700
win_height = 500
display.set_caption('shooter')
background = transform.scale(image.load("galaxy.jpg"),(700, 500))
sprite1 = Player("rocket.png", 10, 425, 5)

monsters = sprite.Group()
for i in range(5):
    monsters.add(Enemy("ufo.png", randint(1, 635), 1, randint(1, 2)))
asteroids = sprite.Group()
for i in range(2):
    asteroids.add(Asteroid("asteroid.png", randint(1, 635), 1, 1))
bullets = sprite.Group()

font.init()
font1 = font.SysFont('Arial', 36)
lost = 0

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255, 215, 0))

mixer.init()
mixer.music.load('space.ogg')
fire = mixer.Sound('fire.ogg')

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        sprite1.reset()
        sprite1.update()
        sprite1.fire()
        monsters.update()
        monsters.draw(window)
        asteroids.update()
        asteroids.draw(window)
        bullets.draw(window)
        bullets.update()

        text_lose = font1.render("Пропущено:" + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (1, 1))

        sprite_list = sprite.spritecollide(sprite1, monsters, False)
        sprite_list = sprite.spritecollide(sprite1, asteroids, True)
        if sprite.groupcollide(monsters, bullets, True, True):
            monsters.add(Enemy("ufo.png", randint(1, 635), 1, randint(1, 2)))

    display.update()