import pygame
import random
from config import *


class AppleManager:
    def __init__(self, screen, snake, color):
        self.apple = Apple(screen, snake, color)
        self.snake = snake
        self.screen = screen
        self.color = color

    def manage(self):

        if not self.apple.spawned and self.snake.alive:
            self.apple.spawn()
            self.apple.spawned = True
        if not self.snake.alive:
            self.apple.spawned = False
        if not self.apple.eaten:
            self.apple.update()
            self.apple.draw()
        else:
            self.apple = Apple(self.screen, self.snake, self.color)


class Apple:
    def __init__(self, screen, snake, color):
        self.eaten = False
        self.spawned = False
        self.screen = screen
        self.color = color
        self.snake = snake
        self.rect = pygame.rect.Rect(0, 0, 0, 0)
        self.x = None
        self.y = None

    def spawn(self):
        while True:
            self.x = random.randint(0, NUMBER_PIXEL-1)
            self.y = random.randint(0, NUMBER_PIXEL-1)

            if not (self.x, self.y) in self.snake.squares:
                self.rect = pygame.rect.Rect(self.x * PIXEL_SIZE, self.y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
                return

    def update(self):
        if (self.x, self.y) in self.snake.squares:
            self.eaten = True
            self.snake.eat = True
            self.snake.score += 1

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
