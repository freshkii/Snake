import pygame
from config import *


class Snake:
    def __init__(self, screen, color):
        self.screen = screen
        self.alive = True
        self.squares = [(5, 10), (6, 10), (7, 10)]
        self.color = color
        self.direction = "right"
        self.last_direction = "right"
        self.eat = False
        self.score = 0
        self.best_score = 0
        self.last_time = 0
        self.velocity = 8

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.alive:
                if event.key == pygame.K_UP and not self.last_direction == "down" and not self.direction == "up":
                    self.direction = "up"
                if event.key == pygame.K_DOWN and not self.last_direction == "up" and not self.direction == "down":
                    self.direction = "down"
                if event.key == pygame.K_LEFT and not self.last_direction == "right" and not self.direction == "left":
                    self.direction = "left"
                if event.key == pygame.K_RIGHT and not self.last_direction == "left" and not self.direction == "right":
                    self.direction = "right"
            else:
                if event.key == pygame.K_RETURN:
                    self.alive = True

    def update(self):
        if self.alive:
            current_time = pygame.time.get_ticks() / 10

            if current_time - self.last_time >= self.velocity:
                new_square = (0, 0)

                # creating new square
                if self.direction == "right":
                    new_square = (self.squares[-1][0] + 1, self.squares[-1][1])
                    if new_square[0] > NUMBER_PIXEL - 1 or new_square in self.squares:
                        self.alive = False
                        return
                    self.last_direction = "right"

                elif self.direction == "left":
                    new_square = (self.squares[-1][0] - 1, self.squares[-1][1])
                    if new_square[0] < 0 or new_square in self.squares:
                        self.alive = False
                        return
                    self.last_direction = "left"

                elif self.direction == "up":
                    new_square = (self.squares[-1][0], self.squares[-1][1] - 1)
                    if new_square[1] < 0 or new_square in self.squares:
                        self.alive = False
                        return
                    self.last_direction = "up"

                elif self.direction == "down":
                    new_square = (self.squares[-1][0], self.squares[-1][1] + 1)
                    if new_square[1] > NUMBER_PIXEL - 1 or new_square in self.squares:
                        self.alive = False
                        return
                    self.last_direction = "down"

                # adding new square
                self.squares.append(new_square)

                if not self.eat:
                    self.squares.pop(0)
                else:
                    self.eat = False
                self.last_time = current_time
        else:
            if self.score > self.best_score:
                self.best_score = self.score
            self.score = 0
            self.eat = False
            self.squares = [(5, 10), (6, 10), (7, 10)]
            self.direction = "right"
            self.last_direction = "right"

    def draw(self):
        for square in self.squares:
            rect = pygame.rect.Rect(square[0] * PIXEL_SIZE, square[1] * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)

            pygame.draw.rect(self.screen, self.color, rect)