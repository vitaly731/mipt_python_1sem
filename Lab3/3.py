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
#Солнце
line(screen, yellow, (420, -50), (400, 270), width=30)
line(screen, yellow, (240, 120), (560, 140), width=30)
arc(screen, yellow, (240, -50, 320, 320), 0, 8*pi, width=30)

k = 0.6
dx = -40
dy = -100

def bear(k, dx, dy):
    #Лужа
    ellipse(screen, dark_grey, (330*k + dx, 550*k + dy, 190*k, 80*k)) 
    arc(screen, black, (330*k + dx, 550*k + dy, 190*k, 80*k), 0, 2*pi, 1)
    ellipse(screen, teal, (345*k + dx, 570*k + dy, 160*k, 58*k))
    arc(screen, black, (345*k + dx, 570*k + dy, 160*k, 58*k), 0, 2*pi, 1)
    #Голова
    ellipse(screen, grey, (120*k + dx, 330*k + dy, 110*k, 80*k))
    arc(screen, black, (120*k + dx, 330*k + dy, 110*k, 80*k), 0, 2*pi, 1)
    #Рот
    line(screen, black, (220*k + dx, 390*k + dy), (170*k + dx, 380*k + dy), width=1)
    #Глаз
    ellipse(screen, black, (166*k + dx, 343*k + dy, 17*k, 12*k))
    #Ухо
    ellipse(screen, grey, (126*k + dx, 329*k + dy, 22*k, 19*k))
    arc(screen, black, (126*k + dx, 329*k + dy, 22*k, 19*k), 0, 2*pi, width=1)
    #Нос
    ellipse(screen, black, (222*k + dx, 355*k + dy, 11*k, 9*k))
    #Туловище
    ellipse(screen, grey, (10*k + dx, 370*k + dy, 180*k, 370*k))
    arc(screen, black, (10*k + dx, 370*k + dy, 180*k, 370*k), 0, 3*pi, 1)
    #Нога, большая часть
    ellipse(screen, grey, (120*k + dx, 620*k + dy, 120*k, 110*k))
    arc(screen, black, (120*k + dx, 620*k + dy, 120*k, 110*k), 0, 3*pi, 1)
    #Нога, маленькая часть
    ellipse(screen, grey, (160*k + dx, 700*k + dy, 120*k, 50*k))
    arc(screen, black, (160*k + dx, 700*k + dy, 120*k, 50*k), 0, 3*pi, 1)
    #Удочка
    line(screen, black, (201*k + dx, 535*k + dy), (219*k + dx, 484*k + dy), width=4)
    line(screen, black, (228*k + dx, 476*k + dy), (446*k + dx, 308*k + dy), width=4)
    line(screen, black, (446*k + dx, 308*k + dy), (448*k + dx, 600*k + dy), width=1)
    #Рука
    ellipse(screen, grey, (158*k + dx, 464*k + dy, (246-158)*k, (507-464)*k))
    arc(screen, black, (158*k + dx, 464*k + dy, (246-158)*k, (507-464)*k), 0, 2*pi, width=1)
    #Рыба
    ellipse(screen, fishy, (430*k + dx, 677*k + dy, 83*k, 33*k))
    arc(screen, black, (430*k + dx, 677*k + dy, 83*k, 33*k), 0, 2*pi, width=1)
    polygon(screen, taily, [[431*k + dx, 690*k + dy], [401*k + dx, 680*k + dy], [401*k + dx, 715*k + dy]])
    aalines(screen, black, True, [[431*k + dx, 690*k + dy], [401*k + dx, 680*k + dy], [401*k + dx, 715*k + dy]])
    ellipse(screen, deep_blue, (496*k + dx, 688*k + dy, 7*k, 6*k))

sets_of_parametres = ((0.55, 400, 420), (0.43, 0, 450), (0.3, 230, 380), (0.2, 440, 380))

for k, dx, dy in sets_of_parametres:
    bear(k, dx, dy)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
