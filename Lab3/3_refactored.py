import pygame
from pygame.draw import *
from math import sin, cos, pi

# Цвета
LIGHT_GREEN = (80, 240, 80)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (50, 50, 255)
LIGHT_RED = (255, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_picture(screen, x, y, width, height):
    '''
    Функция рисует домик с крышей и окном, а также дерево
    на фоне зелёной травы и синего неба с солнцем и облаком.
    
    screen - дисплей pygame, на котором происходит рисование
    x, y - координаты левого верхнего угла прямоугольника с картинкой
    width, height - ширина и высота прямоугольника с картинкой
    '''
    draw_background(screen, x, y, width, height)
    sun_x = 1 / 18 * width
    sun_y = 1 / 12 * height
    sun_radius = min(width, height) / 15
    draw_sun(screen, sun_x, sun_y, sun_radius)
    cloud_x = 4 / 15 * width
    cloud_y = 1 / 5 * height
    cloud_width = 5 / 26 * width
    draw_cloud(screen, cloud_x, cloud_y, cloud_width)
    cloud_x = 27 / 50 * width
    cloud_y = 7 / 24 * height
    cloud_width = 5 / 36 * width
    draw_cloud(screen, cloud_x, cloud_y, cloud_width)
    cloud_x = 87 / 100 * width
    cloud_y = 7 / 25 * height
    cloud_width = 1 / 5 * width
    draw_cloud(screen, cloud_x, cloud_y, cloud_width)
    tree_x = 8 / 23 * width
    tree_y = 7 / 20 * height
    tree_height = 7 / 30 * height
    draw_tree(screen, tree_x, tree_y, tree_height)
    tree_x = 10 / 13 * width
    tree_y = 1 / 3 * height
    tree_height = 1 / 6 * height
    draw_tree(screen, tree_x, tree_y, tree_height)
    house_x = 1 / 9 * width
    house_y = 2 / 5 * height
    house_width = 2 / 9 * width
    draw_house(screen, house_x, house_y, house_width)
    house_x = 5 / 9 * width
    house_y = 2 / 5 * height
    house_width = 9 / 50 * width
    draw_house(screen, house_x, house_y, house_width)

def draw_background(screen, x, y, width, height):
    '''
    Функция рисует фон: траву и небо.

    screen - дисплей pygame, на котором происходит рисование
    x, y - координаты левого верхнего угла прямоугольника с фоном
    width, height - ширина и высота прямоугольника с фоном
    '''
    sky_height = height / 2
    rect(screen, BLUE, (0, 0, width, sky_height)) # Небо
    rect(screen, LIGHT_GREEN,
         (0, sky_height, width, height - sky_height)) # Трава
    
def draw_sun(screen, x, y, radius):
    '''
    Функция рисует солнце.
    
    screen - дисплей pygame, на котором происходит рисование
    x, y - координаты центра солнца
    radius - радиус солнца
    '''
    n = 20 # Число солнечных лучей
    outer_radius = radius
    inner_radius = 19 / 20 * outer_radius
    polygon_points = []
    for i in range(n * 2):
        angle = 2 * pi * i / (2 * n)
        if i % 2 == 0:
            bias_x = outer_radius * cos(angle)
            bias_y = outer_radius * sin(angle)
        else:
            bias_x = inner_radius * cos(angle)
            bias_y = inner_radius * sin(angle)
        point_x = x + bias_x
        point_y = y + bias_y
        polygon_points.append((point_x, point_y))
    polygon(screen, LIGHT_RED, polygon_points) # Заливка
    polygon(screen, BLACK, polygon_points, width=1) # Контур 

def draw_cloud(screen, x, y, width):
    '''
    Функция рисует облако.

    screen - дисплей pygame, на котором происходит рисование
    x, y - координаты опорной точки облака
    Опорная точка лежит на середине нижней стороны прямоугольника,
    описанного вокруг облака
    width - ширина прямоугольника, описанного вокруг облака
    '''
    r = width / 5
    central_points = [(-3/2 * r, -r), (-1/2 * r, -r), (1/2 * r, -r), (3/2 * r, -r),
                      (-1/2 * r, -2 * r), (1/2 * r, -2 * r)]
    for (bias_x, bias_y) in central_points:
        circle(screen , WHITE, (x + bias_x, y + bias_y), r)
        circle(screen , BLACK, (x + bias_x, y + bias_y), r, width=1)

def draw_tree(screen, x, y, height):
    '''
    Функция рисует дерево.

    screen - дисплей pygame, на котором происходит рисование
    x, y - координаты левого верхнего угла прямоугольника, описанного вокруг дерева
    height - высота прямоугольника, описанного вокруг дерева
    '''
    s = height
    k = 0.8
    rect(screen, BLACK, (x + s * 3 / 7, y + s * k, s / 7, s))
    circle(screen, BRIGHT_GREEN, (x + s / 2, y + s * k / 4), s / 4)
    circle(screen, BLACK, (x + s / 2, y + s * k / 4), s / 4, width=1)
    circle(screen, BRIGHT_GREEN, (x + s / 4, y + s * k / 2), s / 4)
    circle(screen, BLACK, (x + s / 4, y + s * k / 2), s / 4, width=1)
    circle(screen, BRIGHT_GREEN, (x + s * 3 / 4, y + s * k / 2), s / 4)
    circle(screen, BLACK, (x + s * 3 / 4, y + s * k / 2), s / 4, width=1)
    circle(screen, BRIGHT_GREEN, (x + s / 2, y + s * k * 3 / 4), s / 4)
    circle(screen, BLACK, (x + s / 2, y + s * k * 3 / 4), s / 4, width=1)
    circle(screen, BRIGHT_GREEN, (x + s / 4, y + s * k), s / 4)
    circle(screen, BLACK, (x + s / 4, y + s * k), s / 4, width=1)
    circle(screen, BRIGHT_GREEN, (x + s * 3 / 4, y + s * k), s / 4)
    circle(screen, BLACK, (x + s * 3 / 4, y + s * k), s / 4, width=1)

def draw_house(screen, x, y, width):
    '''
    Функция рисует дом.

    screen - дисплей pygame, на котором происходит рисование
    x, y - координаты левого верхнего угла прямоугольника, описанного вокруг дерева
    width - ширина дома (ширина прямоугольника, описанного вокруг дерева)
    '''
    s = width / 2
    rect(screen, (204, 119, 34), (x, y + s, 2 * s, int(1.5 * s)))
    rect(screen, (0, 0, 0), (x, y + s, 2 * s, int(1.5 * s)), 1)
    rect(screen, (150, 150, 255), (x + s * 3 // 4, y + int(1.5 * s),
                                       s // 2, s // 2))
    rect(screen, (190, 100, 34), (x + s * 3 // 4, y + int(1.5 * s),
                                      s // 2, s // 2), 5)
    polygon(screen, (255, 100, 100), [(x, y + s), (x + s, y), (x + 2 * s,
                                                                   y + s)], 0)
    polygon(screen, (0, 0, 0), [(x, y + s), (x + s, y), (x + 2 * s,
                                                             y + s)], 1)
    kt = 13
    for i in range(kt + 1):
        polygon(screen, (100, 100, 100), [(x + s - i * int(s // kt),
                                               y + i * int(s // kt)),
                                              (x + s - (i + 1) * int(s // kt),
                                               y + (i + 1) * int(s // kt)),
                                              (x + s - i * int(s // kt),
                                               y + (i + 1) * int(s // kt))], 0)
    for i in range(kt + 1):
        polygon(screen, (100, 100, 100), [(x + s + i * int(s // kt),
                                               y + i * int(s // kt)),
                                              (x + s + (i + 1) * int(s // kt),
                                               y + (i + 1) * int(s // kt)),
                                              (x + s + i * int(s // kt),
                                               y + (i + 1) * int(s // kt))], 0)

pygame.init()

FPS = 30
width, height = 910, 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

draw_picture(screen, 0, 0, width, height)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
