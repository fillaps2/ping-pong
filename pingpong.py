from pygame import *


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

win_width = 900
win_height = 600
window = display.set_mode((win_width, win_height))
background = (100,00,100)
window.fill(background)

skovorodka_left = Player('racket.png', 30, 250, 4, 50, 150)
skovorodka_right = Player('racket.png', 830, 250, 4, 50, 150)
pimpimpampambrrrbrrrpatapim = GameSprite('tenis_ball.png', 200,200,4,50,50)


game = True
finish = False
FPS = 144
clock = time.Clock()

font.init()
font = font.Font(None,35)
lirililarila = font.render('Player 1 lose!', True, (255,0,0))
bobritobondito = font.render('Player 2 lose!', True, (255,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        skovorodka_left.update_l()
        skovorodka_right.update_r()
        pimpimpampambrrrbrrrpatapim.rect.x += speed_x
        pimpimpampambrrrbrrrpatapim.rect.y += speed_y

        if sprite.collide_rect(skovorodka_left, pimpimpampambrrrbrrrpatapim) or sprite.collide_rect(skovorodka_right, pimpimpampambrrrbrrrpatapim):
            speed_x *= -1

        if pimpimpampambrrrbrrrpatapim.rect.y > win_height-50 or pimpimpampambrrrbrrrpatapim.rect.y <0:
            speed_y *= -1
        
        if pimpimpampambrrrbrrrpatapim.rect.x < 0:
            finish = True
            window.blit(lirililarila, (350,280))

        if pimpimpampambrrrbrrrpatapim.rect.x >win_width:
            finish = True
            window.blit(bobritobondito, (350,280))    

        skovorodka_left.reset()
        skovorodka_right.reset()

        pimpimpampambrrrbrrrpatapim.reset()
    
    display.update()
    clock.tick(FPS)


