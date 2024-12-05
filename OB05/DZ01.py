import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH = 800
HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Параметры ракеток и мяча
paddle_width = 15
paddle_height = 100
ball_size = 15

# Начальные позиции
paddle1_x = 30
paddle2_x = WIDTH - paddle_width - 30
paddle1_y = HEIGHT // 2 - paddle_height // 2
paddle2_y = HEIGHT // 2 - paddle_height // 2
ball_x = WIDTH // 2 - ball_size // 2
ball_y = HEIGHT // 2 - ball_size // 2

# Начальная скорость мяча
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# Скорость ракеток
paddle_speed = 7
computer_speed = 5  # Скорость компьютера

# Очки
score1 = 0
score2 = 0

# Шрифт для отображения очков
font = pygame.font.SysFont('Arial', 30)

# Основной цикл игры
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление ракеткой игрока
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle1_y < HEIGHT - paddle_height:
        paddle1_y += paddle_speed

    # Управление компьютером (вторая ракетка)
    if ball_speed_x > 0:  # Если мяч идет в сторону компьютера
        # Простое следование за мячом
        if paddle2_y + paddle_height / 2 < ball_y + ball_size / 2:
            paddle2_y += computer_speed
        elif paddle2_y + paddle_height / 2 > ball_y + ball_size / 2:
            paddle2_y -= computer_speed

        # Вводим ошибку в поведение компьютера
        if random.random() < 0.2:  # 20% ошибок
            paddle2_y += random.choice([-1, 1]) * random.randint(0, 10)

        # Компьютер может сделать ошибку на больших скоростях мяча
        if abs(ball_speed_x) > 8:  # Когда мяч движется быстро
            if random.random() < 0.3:  # 30% вероятность ошибки
                paddle2_y += random.choice([-1, 1]) * random.randint(0, 15)

    # Ограничение движения ракетки компьютера (чтобы она не выходила за пределы)
    if paddle2_y < 0:
        paddle2_y = 0
    elif paddle2_y > HEIGHT - paddle_height:
        paddle2_y = HEIGHT - paddle_height

    # Движение мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Отражение мяча от верхней и нижней границы
    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y = -ball_speed_y

    # Отражение мяча от ракеток
    if (ball_x <= paddle1_x + paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height):
        # Мяч отскакивает от ракетки игрока
        ball_speed_x = -ball_speed_x
        # Учитываем скорость ракетки при отскоке
        speed_factor = (paddle1_y + paddle_height / 2 - ball_y) / (paddle_height / 2)  # [-1, 1]
        ball_speed_y += speed_factor * 3  # Увеличиваем влияние на вертикальную скорость мяча

    if (ball_x >= paddle2_x - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height):
        # Мяч отскакивает от ракетки компьютера
        ball_speed_x = -ball_speed_x
        # Учитываем скорость ракетки при отскоке
        speed_factor = (paddle2_y + paddle_height / 2 - ball_y) / (paddle_height / 2)  # [-1, 1]
        ball_speed_y += speed_factor * 3  # Увеличиваем влияние на вертикальную скорость мяча

    # Если мяч выходит за пределы экрана (гол)
    if ball_x <= 0:
        score2 += 1
        ball_x = WIDTH // 2 - ball_size // 2
        ball_y = HEIGHT // 2 - ball_size // 2
        ball_speed_x = 5 * random.choice((1, -1))
        ball_speed_y = 5 * random.choice((1, -1))

    if ball_x >= WIDTH - ball_size:
        score1 += 1
        ball_x = WIDTH // 2 - ball_size // 2
        ball_y = HEIGHT // 2 - ball_size // 2
        ball_speed_x = 5 * random.choice((1, -1))
        ball_speed_y = 5 * random.choice((1, -1))

    # Отображение счета
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Отображение ракеток и мяча
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))

    # Обновление экрана
    pygame.display.flip()

# Закрытие Pygame
pygame.quit()
