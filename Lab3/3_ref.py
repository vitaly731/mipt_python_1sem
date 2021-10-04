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

def bear(k, dx, dy):
    #Полынья
    x = 330*k + dx
    y = 550*k + dy
    x_size = 190*k
    y_size = 80*k
    ellipse(screen, dark_grey, (x, y, x_size, y_size)) 
    arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
    x = 345*k + dx
    y = 570*k + dy
    x_size = 160*k
    y_size = 58*k
    ellipse(screen, teal, (x, y, x_size, y_size))
    arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
    #Голова
    x = 120*k + dx
    y = 330*k + dy
    x_size = 110*k
    y_size = 80*k
    ellipse(screen, grey, (x, y, x_size, y_size))
    arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
    #Рот
    x1 = 220*k + dx
    y1 = 390*k + dy
    x2 = 170*k + dx
    y2 = 380*k + dy
    line(screen, black, (x1, y1), (x2, y2), width=1)
    #Глаз
    x = 166*k + dx
    y = 343*k + dy
    x_size = 17*k
    y_size = 12*k
    ellipse(screen, black, (x, y, x_size, y_size))
    #Ухо
    x = 126*k + dx
    y = 329*k + dy
    x_size = 22*k
    y_size = 19*k
    ellipse(screen, grey, (x, y, x_size, y_size))
    arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
    #Нос
    x = 222*k + dx
    y = 355*k + dy
    x_size = 11*k
    y_size = 9*k
    ellipse(screen, black, (x, y, x_size, y_size))
    #Туловище
    x = 10*k + dx
    y = 370*k + dy
    x_size = 180*k
    y_size = 370*k
    ellipse(screen, grey, (x, y, x_size, y_size))
    arc(screen, black, (x, y, x_size, y_size), 0, 3*pi)
    #Нога, большая часть
    x = 120*k + dx
    y = 620*k + dy
    x_size = 120*k
    y_size = 110*k
    ellipse(screen, grey, (x, y, x_size, y_size))
    arc(screen, black, (x, y, x_size, y_size), 0, 3*pi)
    #Нога, маленькая часть
    x = 160*k + dx
    y = 700*k + dy
    x_size = 120*k
    y_size = 50*k
    ellipse(screen, grey, (x, y, x_size, y_size))
    arc(screen, black, (x, y, x_size, y_size), 0, 3*pi)
    #Удочка
    x1 = 201*k + dx
    y1 = 535*k + dy
    x2 = 219*k + dx
    y2 = 484*k + dy
    line(screen, black, (x1, y1), (x2, y2), width=4)
    x1 = 228*k + dx
    y1 = 476*k + dy
    x2 = 446*k + dx
    y2 = 308*k + dy
    line(screen, black, (x1, y1), (x2, y2), width=4)
    x1 = 446*k + dx
    y1 = 308*k + dy
    x2 = 448*k + dx
    y2 = 600*k + dy
    line(screen, black, (x1, y1), (x2, y2), width=1)
    #Рука
    x = 158*k + dx
    y = 464*k + dy
    x_size = 88*k
    y_size = 43*k
    ellipse(screen, grey, (x, y, x_size, y_size))
    arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
    #Рыба
    x = 430*k + dx
    y = 677*k + dy
    x_size = 83*k
    y_size = 33*k
    ellipse(screen, fishy, (x, y, x_size, y_size))
    arc(screen, black, (x, y, x_size, y_size), 0, 2*pi)
    x1 = 431*k + dx
    y1 = 690*k + dy
    x2 = 401*k + dx
    y2 = 680*k + dy
    x3 = 401*k + dx
    y3 = 715*k + dy
    polygon(screen, taily, [[x1, y1], [x2, y2], [x3, y3]])
    aalines(screen, black, True, [[x1, y1], [x2, y2], [x3, y3]])
    x = 496*k + dx
    y = 688*k + dy
    x_size = 7*k
    y_size = 6*k
    ellipse(screen, deep_blue, (x, y, x_size, y_size))

sets_of_parametres = ()
A = list(sets_of_parametres)
A.append((0.55, 400, 420))
A.append((0.43, 0, 450))
A.append((0.3, 230, 380))
A.append((0.2, 440, 380))
sets_of_parametres = tuple(A)

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
