import pygame
import time
import pygame as pg

pygame.init()


class Button:
    first_click = time.time()
    button = False

    def __init__(self, window, size, x, y, color, text="", txtsize=0):
        self.size = size
        self.window = window
        self.color = color
        self.text = text
        self.txtsize = txtsize
        self.x = x
        self.y = y

    def place(self):
        x = self.x
        y = self.y

        pygame.draw.rect(self.window, self.color, (x, y, self.size[0], self.size[1]))
        f = pygame.font.Font("C:\Windows\Fonts\calibri.ttf", self.txtsize)
        t = f.render(self.text, False, (0, 0, 0) if self.color != (0, 0, 0) else (255, 255, 255))
        self.window.blit(t, (x + 5, y + 5))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if time.time() - self.__class__.first_click > 0.2 and pygame.mouse.get_pressed()[0] and (
                mouse_pos[0] in range(self.x, self.x + self.size[0])) and (
                mouse_pos[1] in range(self.y, self.y + self.size[1])):
            self.__class__.first_click = time.time()

            return True


class PopUp:
    def __init__(self, window, windowsize, size, type, text, txtsize):
        self.txtsize = txtsize
        self.text = text
        self.windowsize = windowsize
        self.window = window
        self.size = size
        self.type = type
        self.activated = False
        self.txts = {}
        self.once = True
        if self.once:
            self.ok_or_cancel = None
            self.once = False

    def activate(self):

        a = 0
        f = pygame.font.SysFont("Myriad Pro", self.txtsize)
        for tx in self.text:
            self.txts["t" + str(a)] = f.render(self.text[a], False, (0, 0, 255))
            a += 1
        self.activated = True
        # pygame.draw.rect(self.window, (255, 255, 255), ((0, 0) if self.location == "topleft" else (self.windowsize[
        # 0] / 2 - self.size[0] / 2, self.windowsize[1] - 10), self.size[0], self.size[1]))
        x = self.windowsize[0] / 2 - self.size[0] / 2
        pygame.draw.rect(self.window, (255, 255, 255), (x, 10, self.size[0], self.size[1]))
        #  pygame.draw.rect(self.window, (255, 255, 255), (
        #  0, 0, self.size[0], self.size[1]))
        b = self.txtsize / 2
        for tt in self.txts.values():
            self.window.blit(tt, (x + 5, 10 + b))
            b += b + 10
