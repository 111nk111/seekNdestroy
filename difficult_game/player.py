import pygame
from pygame_classes import *


class Player:
    def __init__(self, borders_x, borders_y):
        self.color = (255, 125, 10)
        self.width = 30
        self.height = 30
        self.size = (self.width, self.height)
        self.x = borders_x[0]
        self.y = borders_y[0]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.borders_x = borders_x
        self.borders_y = borders_y

    def show(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 4
        if keys[pygame.K_d]:
            self.x += 4
        if keys[pygame.K_s]:
            self.y += 3
        if keys[pygame.K_w]:
            self.y -= 3
        if self.x <= self.borders_x[0]:
            self.x = self.borders_x[0]
        if self.x >= self.borders_x[1]:
            self.x = self.borders_x[1]
        if self.y <= self.borders_y[0]:
            self.y = self.borders_y[0]
        if self.y >= self.borders_y[1]:
            self.y = self.borders_y[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)























