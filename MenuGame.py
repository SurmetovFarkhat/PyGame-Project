import sys

import pygame

FPS = 50
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    size_window = [1000, 600]
    screen = pygame.display.set_mode(size_window)

    font_name_game = pygame.font.Font(None, 100)
    text_name_game = font_name_game.render("Python Game!", True, (255, 255, 255))
    screen.blit(text_name_game, (280, 150))

    font_exit = pygame.font.Font(None, 25)
    text_exit = font_exit.render('start', True, (255, 255, 255))
    screen.blit(text_exit, (470, 350))
    button_start = pygame.draw.rect(screen, (255, 255, 255), (290, 350 - 10, 420, 440 - 400), 1)

    font_exit = pygame.font.Font(None, 25)
    text_exit = font_exit.render('exit', True, (255, 255, 255))
    screen.blit(text_exit, (470, 400))
    button_exit = pygame.draw.rect(screen, (255, 255, 255), (290, 400 - 10, 420, 440 - 400), 1)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos):
                    screen.fill((0, 0, 0))
                    # начинаем игру
                elif button_exit.collidepoint(event.pos):
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
