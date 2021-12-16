import pygame
from pygame.draw import circle, rect
from random import randint

pygame.init()

FPS = 80
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
MAX_SPEED = 10
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BALL_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
BLACK = (0, 0, 0)

class Ball():
    def __init__(self):
        self.radius = randint(3, 50)
        self.x = randint(self.radius, SCREEN_WIDTH - self.radius)
        self.y = randint(self.radius, SCREEN_HEIGHT - self.radius)
        self.velocity_x = randint(-MAX_SPEED, MAX_SPEED)
        self.velocity_y = randint(-MAX_SPEED, MAX_SPEED)
        self.color = BALL_COLORS[randint(0, len(BALL_COLORS) - 1)]
        circle(screen, self.color, (self.x, self.y), self.radius, 0)

    '''
    Функция обновляет координаты шарика в соответствии с его скоростью.
    Если шарик подлетает к границам игрового поля, происходит изменение
    направления скорости (вызывается self.reflection).
    В конце рисуется обновленное состояние шарика
    '''
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        if self.x - self.radius < 0: #левая граница
            self.reflection(0, MAX_SPEED, -MAX_SPEED, MAX_SPEED)
        elif self.x + self.radius > SCREEN_WIDTH: #правая граница
            self.reflection(-MAX_SPEED, 0, -MAX_SPEED, MAX_SPEED)
        if self.y - self.radius < 0: #верхняя граница
            self.reflection(-MAX_SPEED, MAX_SPEED, 0, MAX_SPEED)
        elif self.y + self.radius > SCREEN_HEIGHT: #нижняя граница
            self.reflection(-MAX_SPEED, MAX_SPEED, -MAX_SPEED, 0)
        circle(screen, self.color, (self.x, self.y), self.radius, 0)

    def reflection(self, min_velocity_x, max_velocity_x,
                   min_velocity_y, max_velocity_y):
        self.velocity_x = randint(min_velocity_x, max_velocity_x)
        self.velocity_y = randint(min_velocity_y, max_velocity_y)

    '''
    Функция возвращает True, если игрок кликнул по области шарика
    '''
    def hit(self, click):
        if (click.pos[0] - self.x) ** 2 + (click.pos[1] - self.y) ** 2 <= self.radius ** 2:
            return True

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0

#Создание целей
target_list = []
for i in range(randint(3, 10)):
    target_list.append(Ball())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for target in target_list:
                if target.hit(event):
                    score += 1
                    print('Score: ', score)
    screen.fill(BLACK)
    for target in target_list:
        target.update()
    pygame.display.update()


pygame.quit()

