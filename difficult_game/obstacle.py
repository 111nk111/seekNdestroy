import pygame
from pygame_classes import *
import random


class Obstacle:
    def __init__(self, screen):
        self.width = 5
        self.x = random.randrange(101, 850)
        self.y = random.randrange(101, 300)
        self.x_limits = [100, 850]
        self.y_limits = [60, 390]
        self.x_speed = random.choices([0, 1, 2], weights=[5, 2, 1], k=1)[0]
        self.y_speed = 3
        self.screen = screen
        self.circle = pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), self.width)

    def draw(self):
        self.y -= self.y_speed
        self.x += self.x_speed
        if self.x <= self.x_limits[0] or self.x >= self.x_limits[1]:
            self.x_speed = -self.x_speed
        if self.y <= self.y_limits[0] or self.y >= self.y_limits[1]:
            self.y_speed = -self.y_speed
        self.circle = pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), self.width)












