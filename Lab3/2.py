import pygame
from pygame.draw import *
from math import *

pygame.init()

FPS = 30
xx = 600
yy = 800
screen = pygame.display.set_mode((xx, yy))

#Цвета
blue = (0, 255, 255)
deep_blue = (0, 0, 255)
grey = (230, 230, 230)
black = (0, 0, 0)
dark_grey = (80, 80, 80)
teal = (0, 128, 128)
yellow = (255, 255, 0)
fishy = (132, 147, 167)
taily = (255, 99, 71)
#Фон
rect(screen, blue, (0, 0, xx, yy * 4/7))
rect(screen, grey, (0, yy * 4/7, xx, yy))
line(screen, black, (0, yy * 4/7), (xx, yy * 4/7))
#Лужа
ellipse(screen, dark_grey, (330, 550, 190, 80)) 
arc(screen, black, (330, 550, 190, 80), 0, 2*pi, 1)
ellipse(screen, teal, (345, 570, 160, 58))
arc(screen, black, (345, 570, 160, 58), 0, 2*pi, 1)
#Солнце
line(screen, yellow, (420, -50), (400, 270), width=30)
line(screen, yellow, (240, 120), (560, 140), width=30)
arc(screen, yellow, (240, -50, 320, 320), 0, 8*pi, width=30)
#Голова
ellipse(screen, grey, (120, 330, 110, 80))
arc(screen, black, (120, 330, 110, 80), 0, 2*pi, 1)
#Рот
line(screen, black, (220, 390), (170, 380), width=1)
#Глаз
ellipse(screen, black, (166, 343, 17, 12))
#Ухо
ellipse(screen, grey, (126, 329, 22, 19))
arc(screen, black, (126, 329, 22, 19), 0, 2*pi, width=1)
#Нос
ellipse(screen, black, (222, 355, 11, 9))
#Туловище
ellipse(screen, grey, (10, 370, 180, 370))
arc(screen, black, (10, 370, 180, 370), 0, 3*pi, 1)
#Нога, большая часть
ellipse(screen, grey, (120, 620, 120, 110))
arc(screen, black, (120, 620, 120, 110), 0, 3*pi, 1)
#Нога, маленькая часть
ellipse(screen, grey, (160, 700, 120, 50))
arc(screen, black, (160, 700, 120, 50), 0, 3*pi, 1)
#Удочка
line(screen, black, (201, 535), (219, 484), width=4)
line(screen, black, (228, 476), (446, 308), width=4)
line(screen, black, (446, 308), (448, 600), width=1)
#Рука
ellipse(screen, grey, (158, 464, 246-158, 507-464))
arc(screen, black, (158, 464, 246-158, 507-464), 0, 2*pi, width=1)
#Рыба
ellipse(screen, fishy, (430, 677, 83, 33))
arc(screen, black, (430, 677, 83, 33), 0, 2*pi, width=1)
polygon(screen, taily, [[431, 690], [401, 680], [401, 715]])
aalines(screen, black, True, [[431, 690], [401, 680], [401, 715]])
ellipse(screen, deep_blue, (496, 688, 7, 6))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
