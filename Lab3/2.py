import pygame
from pygame.draw import *
from math import *

pygame.init()
FPS = 30

X = 600
Y = 800
screen = pygame.display.set_mode((X, Y))

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
x = 0
y = 0
x_size = X
y_size = Y*4/7
rect(screen, blue, (x, y, x_size, y_size))
x = 0
y = Y*4/7
x_size = X
y_size = Y*3/7
rect(screen, grey, (x, y, x_size, y_size))
x1 = 0
y1 = Y*4/7
x2 = X
y2 = Y*4/7
line(screen, black, (x1, y1), (x2, y2))
#Солнце
x1 = 420
y1 = -50
x2 = 400
y2 = 270
line(screen, yellow, (x1, y1), (x2, y2), width=30)
x1 = 240
y1 = 120
x2 = 560
y2 = 140
line(screen, yellow, (x1, y1), (x2, y2), width=30)
x = 240
y = -50
x_size = 320
y_size = 320
arc(screen, yellow, (x, y, x_size, y_size), 0, 8*pi, width=30)
#Полынья
x = 330
y = 550
x_size = 190
y_size = 80
ellipse(screen, dark_grey, (x, y, x_size, y_size)) 
arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
x = 345
y = 570
x_size = 160
y_size = 58
ellipse(screen, teal, (x, y, x_size, y_size))
arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
#Голова
x = 120
y = 330
x_size = 110
y_size = 80
ellipse(screen, grey, (x, y, x_size, y_size))
arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
#Рот
x1 = 220
y1 = 390
x2 = 170
y2 = 380
line(screen, black, (x1, y1), (x2, y2), width=1)
#Глаз
x = 166
y = 343
x_size = 17
y_size = 12
ellipse(screen, black, (x, y, x_size, y_size))
#Ухо
x = 126
y = 329
x_size = 22
y_size = 19
ellipse(screen, grey, (x, y, x_size, y_size))
arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
#Нос
x = 222
y = 355
x_size = 11
y_size = 9
ellipse(screen, black, (x, y, x_size, y_size))
#Туловище
x = 10
y = 370
x_size = 180
y_size = 370
ellipse(screen, grey, (x, y, x_size, y_size))
arc(screen, black, (x, y, x_size, y_size), 0, 3*pi)
#Нога, большая часть
x = 120
y = 620
x_size = 120
y_size = 110
ellipse(screen, grey, (x, y, x_size, y_size))
arc(screen, black, (x, y, x_size, y_size), 0, 3*pi)
#Нога, маленькая часть
x = 160
y = 700
x_size = 120
y_size = 50
ellipse(screen, grey, (x, y, x_size, y_size))
arc(screen, black, (x, y, x_size, y_size), 0, 3*pi)
#Удочка
x1 = 201
y1 = 535
x2 = 219
y2 = 484
line(screen, black, (x1, y1), (x2, y2), width=4)
x1 = 228
y1 = 476
x2 = 446
y2 = 308
line(screen, black, (x1, y1), (x2, y2), width=4)
x1 = 446
y1 = 308
x2 = 448
y2 = 600
line(screen, black, (x1, y1), (x2, y2), width=1)
#Рука
x = 158
y = 464
x_size = 88
y_size = 43
ellipse(screen, grey, (x, y, x_size, y_size))
arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
#Рыба
x = 430
y = 677
x_size = 83
y_size = 33
ellipse(screen, fishy, (x, y, x_size, y_size))
arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
x1 = 431
y1 = 690
x2 = 401
y2 = 680
x3 = 401
y3 = 715
polygon(screen, taily, [[x1, y1], [x2, y2], [x3, y3]])
aalines(screen, black, True, [[x1, y1], [x2, y2], [x3, y3]])
x = 496
y = 688
x_size = 7
y_size = 6
ellipse(screen, deep_blue, (x, y, x_size, y_size))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
