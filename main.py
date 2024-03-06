import pygame
import sys
import random
import time

start_time = None
end_time = None

# Установка размеров окна и клетчатого поля
WINDOW_SIZE = 500
CELL_SIZE = 50
GRID_SIZE = 5


def generate_goal_position():
    goal_x = 0
    goal_y = 0
    while goal_x == 0 and goal_y == 0:
        goal_x = random.randint(0, GRID_SIZE - 1)
        goal_y = random.randint(0, GRID_SIZE - 1)
    return (goal_x, goal_y)


goal_position = generate_goal_position()

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Создание окна
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Simple Game")


# Функция отрисовки клетчатого поля
def draw_grid():
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(window, BLACK, (x, 0), (x, WINDOW_SIZE))
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(window, BLACK, (0, y), (WINDOW_SIZE, y))


# Функция отрисовки персонажа
def draw_character(x, y):
    player_image = pygame.image.load("player.png")
    player_rect = player_image.get_rect()
    player_rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
    window.blit(player_image, player_rect)


# Функция отрисовки цели


gate_image = pygame.image.load("gate.png")
gate_image = pygame.transform.scale(gate_image, (CELL_SIZE, CELL_SIZE))


# Игровой цикл
def game_loop():
    global start_time
    x = 0
    y = 0
    goal_position = (generate_goal_position())  # Позиция цели

    def draw_goal():
        x, y = goal_position
        window.blit(gate_image, (x * CELL_SIZE, y * CELL_SIZE))

    # Внутри game_loop() после отрисовки игрока и препятствий
    draw_goal()

    while True:
        window.fill(WHITE)
        draw_grid()
        draw_character(x, y)
        draw_goal()
        pygame.display.update()
        if start_time is None:
            start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 1
                if event.key == pygame.K_RIGHT:
                    x += 1
                if event.key == pygame.K_UP:
                    y -= 1
                if event.key == pygame.K_DOWN:
                    y += 1

            if x == goal_position[0] and y == goal_position[1]:
                font = pygame.font.Font(None, 48)
                congrats_text = font.render("Вы прошли игру!", True, GREEN)
                text_rect = congrats_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
                window.blit(congrats_text, text_rect)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Поздравляем! Вы достигли цели за {elapsed_time:.2f} секунд.")
                stats_font = pygame.font.Font(None, 24)
                elapsed_time_text = stats_font.render(f"Time: {elapsed_time:.2f} sec", True, (255, 255, 255))
                window.blit(elapsed_time_text, (10, 10))
                pygame.display.update()
                pygame.time.wait(2000)  # Подождать 2 секунды перед завершением игры
                pygame.quit()
                sys.exit()


# Начальный экран
start_button = pygame.Rect(200, 200, 100, 50)
exit_button = pygame.Rect(200, 300, 100, 50)

while True:
    window.fill(WHITE)

    # Отображение кнопок "start" и "exit"
    pygame.draw.rect(window, BLACK, start_button)
    pygame.draw.rect(window, BLACK, exit_button)

    font = pygame.font.Font(None, 36)
    start_text = font.render("Start", True, WHITE)
    exit_text = font.render("Exit", True, WHITE)
    window.blit(start_text, (215, 215))
    window.blit(exit_text, (220, 315))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if start_button.collidepoint(mouse_pos):
                game_loop()
            if exit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    pygame.display.update()
