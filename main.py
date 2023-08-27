import pygame
from config import *
import snake
from apple import AppleManager
from score import show_score
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 30)

snake = snake.Snake(screen, "#4682b4")

apple_manager = AppleManager(screen, snake, "#e60000")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        snake.handle_event(event)

    snake.update()

    screen.fill("#00ff00")

    apple_manager.manage()

    snake.draw()

    show_score(screen, font, snake)

    pygame.display.update()
    clock.tick(60)