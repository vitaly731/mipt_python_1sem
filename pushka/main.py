import math
from random import choice, randint

import pygame

FPS = 30
MAX_TIME = 100

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GOLD = (249, 166, 2)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen: pygame.Surface, x, y, type='classic'): 
        """
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 15
        self.v_x = 0
        self.v_y = 0
        if type == 'black':
            self.color = BLACK
        elif type == 'grey':
            self.color = GREY
        elif type == 'bomb':
            self.color = GOLD
        else:
            self.color = choice(GAME_COLORS)
        self.type = type
        self.live = 30
        self.gravity = 0
        self.time = 0

    def move(self, gravity_flag=True):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.v_x и self.v_y, силы гравитации, действующей на мяч,
        и стен по краям окна.
        """
        self.x += int(self.v_x)
        if gravity_flag:
            self.y -= int(self.v_y - self.gravity)
        else:
            self.y -= int(self.v_y + self.gravity)
        if self.x + self.r > WIDTH:
            self.x = WIDTH - self.r
            self.v_x = -self.v_x * 0.8
            if self.v_y > 0:
                self.v_y = self.v_y - 1
                if self.v_y < 1:
                    self.v_y = 0
            if self.v_y < 0:
                self.v_y = self.v_y + 1
                if self.v_y > 1:
                    self.v_y = 0
            self.gravity = 0
        if self.y + self.r > HEIGHT:
            self.y = HEIGHT - self.r
            self.v_y = -self.v_y * 0.8
            if self.v_x > 0:
                self.v_x = self.v_x - 1
                if self.v_x < 1:
                    self.v_x = 0
                    self.v_y = 0
            if self.v_x < 0:
                self.v_x = self.v_x + 1
                if self.v_x > 1:
                    self.v_x = 0
                    self.v_y = 0
            self.gravity = 0
        self.gravity += 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            int(self.r)
        )

    def is_hit(self, target):
        """
        Функция проверяет сталкивалкивается ли данный объект с целью, описываемой в объекте target.
        target: Объект, с которым проверяется столкновение.
        Returns: Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - target.x) ** 2 + (self.y - target.y) ** 2 <= (self.r + target.r) ** 2:
            return True
        else:
            return False

    def tic(self, balls):
        self.time += 1
        if self.time > 100:
            balls.pop(balls.index(self))
        return balls


class Black_Ball(Ball):
    def __init__(self, screen: pygame.Surface, x, y):
        super().__init__(screen, x, y, 'black')

    def move(self):
        super().move(False)


class Grey_Ball(Ball):
    def __init__(self, screen: pygame.Surface, x, y):
        super().__init__(screen, x, y, 'grey')

    def move(self):
        self.gravity = 0
        super().move()


class Bomb(Ball):
    def __init__(self, screen: pygame.Surface, x, y):
        super().__init__(screen, x, y, 'bomb')

    def is_hit(self, obj):
        if obj.x - 25 - self.r < self.x < obj.x + 25 + self.r and self.y + self.r > obj.y - 20:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = x
        self.y = y
        self.length = 35
        self.width = 7
        self.v = 5

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event, balls, bullet):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        bullet += 1
        if event.button == 3:
            new_ball = Black_Ball(self.screen, self.x, self.y)
        elif event.button == 2:
            new_ball = Grey_Ball(self.screen, self.x, self.y)
        else:
            new_ball = Ball(self.screen, self.x, self.y)
        new_ball.v_x = self.f2_power * math.cos(self.an)
        new_ball.v_y = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        return balls, bullet

    def targetting(self, mouse_x, mouse_y):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            try:
                self.an = math.atan((mouse_y - self.y) / (mouse_x - self.x))
            except ZeroDivisionError:
                self.an = math.atan((mouse_y - self.y) / (mouse_x - self.x + 0.0000000001))
        if mouse_x < self.x:
            self.an = self.an + math.pi
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - self.width // 2 * math.sin(-self.an), self.y - self.width // 2 * math.cos(-self.an)),
             (self.x + self.length * math.cos(-self.an) - self.width // 2 * math.sin(-self.an),
              self.y - self.length * math.sin(-self.an) - self.width // 2 * math.cos(-self.an)),
             (self.x + self.length * math.cos(-self.an) + self.width // 2 * math.sin(-self.an),
              self.y - self.length * math.sin(-self.an) + self.width // 2 * math.cos(-self.an)),
             (self.x + self.width // 2 * math.sin(-self.an), self.y + self.width // 2 * math.cos(-self.an))]
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.length += 1
            self.color = RED
        else:
            self.color = GREY
            self.length = 35

    def move(self, keys, dop_gun):
        if keys[pygame.K_LEFT] and self.x - 25 > 0 and dop_gun.x - 25 > 0:
            self.x -= self.v
            dop_gun.x -= dop_gun.v
        elif keys[pygame.K_RIGHT] and self.x + 25 < WIDTH and dop_gun.x + 25 < WIDTH:
            self.x += self.v
            dop_gun.x += dop_gun.v


class Target:
    def __init__(self, screen: pygame.Surface, color=RED):
        self.points = 0
        self.live = 1
        self.color = color
        self.new_target()
        self.screen = screen
        self.v = 5

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(669, 749)
        self.y = randint(51, 549)
        self.r = randint(2, 50)
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def move(self):
        self.y += self.v
        if self.y + self.r >= HEIGHT or self.y - self.r <= 0:
            self.v = -self.v

    def drop(self, bombs):
        """Сброс бомбы."""
        new_bomb = Bomb(self.screen, self.x, self.y)
        new_bomb.x -= new_bomb.r // 2
        bombs.append(new_bomb)
        return bombs


class Blue_Target(Target):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen, BLUE)

    def move(self):
        self.x += self.v
        if self.x + self.r >= WIDTH or self.x - self.r <= 0:
            self.v = -self.v


class Cyan_Target(Target):
    def __init__(self, screen: pygame.Surface):
        self.teleport_time = 100
        super().__init__(screen, CYAN)

    def move(self):
        if self.teleport_time == 0:
            self.x = randint(669, 749)
            self.y = randint(51, 549)
            self.r = randint(2, 50)
            self.teleport_time = 100
        else:
            self.teleport_time -= 1


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
str_bullet = bullet
balls = []
bombs = []
score = 0

clock = pygame.time.Clock()
gun = Gun(screen, 35, 450)
targets = [Target(screen), Blue_Target(screen), Cyan_Target(screen)]
finished = False
time = MAX_TIME
bomb_time = MAX_TIME

pygame.font.init()
font1 = pygame.font.Font(None, 36)
text_score = font1.render(str(score), True, (0, 0, 0))
text_hit = font1.render('Вы уничтожили цель за ' + str(str_bullet) + ' выстрелов', True, (0, 0, 0))
mouse_x, mouse_y = WIDTH // 2, HEIGHT // 2

while not finished:
    screen.fill(WHITE)
    gun.draw()
    if time == MAX_TIME:
        for t in targets:
            t.draw()
    for b in balls:
        b.draw()
        balls = b.tic(balls)
    for b in bombs:
        b.draw()
        bombs = b.tic(bombs)
    screen.blit(text_score, (0, 0))
    if time < MAX_TIME:
        screen.blit(text_hit, (200, 250))
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if time == MAX_TIME:
                gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            if time == MAX_TIME:
                balls, bullet = gun.fire2_end(event, balls, bullet)
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos[0], event.pos[1]
            gun.targetting(mouse_x, mouse_y)

    keys = pygame.key.get_pressed()
    gun.move(keys, gun)
    gun.targetting(mouse_x, mouse_y)

    for t in targets:
        t.move()
    for b in bombs:
        b.move()
        if b.is_hit(gun):
            score -= 1
            text_score = font1.render(str(score), True, (0, 0, 0))
            bombs.pop(bombs.index(b))
    for b in balls:
        b.move()
        for t in targets:
            if b.is_hit(t) and t.live:
                t.live -= 1
                t.hit()
                t.new_target()
                time = 0
                score += 1
                text_score = font1.render(str(score), True, (0, 0, 0))
                if bullet != 0:
                    str_bullet = bullet
                text_hit = font1.render('Вы уничтожили цель за ' + str(str_bullet) + ' выстрелов', True, (0, 0, 0))
                bullet = 0
                gun.f2_on = False
    gun.power_up()
    if time < MAX_TIME:
        time += 1
    if bomb_time == 0:
        for t in targets:
            bombs = t.drop(bombs)
        bomb_time = MAX_TIME
    else:
        bomb_time -= 1

pygame.quit()
