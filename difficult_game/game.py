import pygame
from pygame_classes import *
from player import Player
from obstacle import Obstacle
import random


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 500))
        x1 = 50
        x2 = 50
        x3 = 850
        x4 = 50
        y1 = 50
        y2 = 50
        y3 = 50
        y4 = 400
        self.game_rect = [pygame.Rect(x1, y1, 2, 350), pygame.Rect(x2, y2, 800, 2), pygame.Rect(x3, y3, 2, 350),
                          pygame.Rect(x4, y4, 800, 2)]
        self.player = Player([x1, x3 - 30], [y1, y4 - 30])
        self.obstacles = [Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen),

                          ]
        self.pixels = []
        self.got = 0
        print(len(self.obstacles))
        for i in range(100, 850, 20):
            for j in range(50, 400, 20):
                self.pixels.append(pygame.Rect(i, j, 10, 10))
        print(len(self.pixels))

    def mainloop(self):
        x1 = 50
        x2 = 50
        x3 = 850
        x4 = 50
        y1 = 50
        y2 = 50
        y3 = 50
        y4 = 400
        self.game_rect = [pygame.Rect(x1, y1, 2, 350), pygame.Rect(x2, y2, 800, 2), pygame.Rect(x3, y3, 2, 350),
                          pygame.Rect(x4, y4, 800, 2)]
        self.player = Player([x1, x3 - 30], [y1, y4 - 30])
        self.obstacles = [Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),
                          Obstacle(self.screen), Obstacle(self.screen),


                          ]
        self.obstacles.sort(key=lambda oo: oo.x)
        self.pixels = []
        self.got = 0
        print(len(self.obstacles))
        for i in range(100, 850, 20):
            for j in range(50, 400, 20):
                self.pixels.append(pygame.Rect(i, j, 10, 10))
        print(len(self.pixels))
        once = False
        clock = pygame.time.Clock()
        while 1:
            self.screen.fill((255, 255, 255))
            clock.tick(60)
            for pp in self.pixels:
                pygame.draw.rect(self.screen, (0, 255, 0), pp)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    exit()
            for s in self.game_rect:
                pygame.draw.rect(self.screen, (255, 0, 0), s)
            self.player.show(self.screen)
            for o in self.obstacles:
                pix = sorted(self.pixels, key=lambda ppp: ppp.x)
                piy = sorted(self.pixels, key=lambda px: px.y, reverse=True)
                o.draw()
                if self.player.rect.colliderect(o.circle):
                    print("LOST")
                    self.game_start("LOST")
                o.x_limits[0] = pix[0].x
                o.y_limits[1] = piy[0].y
                if o.x < o.x_limits[0]:
                    o.x = o.x_limits[0]

            try:
                for p in self.pixels:
                    if self.player.rect.colliderect(p):
                        self.pixels.remove(p)
                        self.got += 1
            except ValueError or IndexError:
                print("WON")
                self.game_start("WON")
            if self.got % 40 == 0 and self.got > 0 and not once:
                try:
                    self.obstacles.sort(key=lambda oo: oo.x)
                    self.obstacles.remove(self.obstacles[0])
                    print(len(self.obstacles))
                except:
                    pass
                self.got += 1

            pygame.display.update()

    def game_start(self, txt):
        font = pygame.font.Font(pygame.font.get_default_font(), 35)
        text = font.render(txt, False, (255, 0, 0))
        while 1:
            self.screen.fill((255, 255, 255))
            btn = Button(self.screen, (100, 50), 400, 200, (0, 0, 0), "START", txtsize=30)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    exit()
            btn.place()
            self.screen.blit(text, (400, 100))
            if btn.check_click():
                self.mainloop()
            pygame.display.update()


g = Game()
g.game_start("")
