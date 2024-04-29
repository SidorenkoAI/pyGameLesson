import pygame
from pygame import Surface
import random
import math
class Ball(pygame.sprite.Sprite):
    def __init__(self, path: str, screen: Surface):
        super().__init__()
        self.screen = screen
        self.orig_img = pygame.image.load(path)
        scale = (50, 50)
        self.orig_img = pygame.transform.scale(surface=self.orig_img, size=scale)
        self.image = self.orig_img.copy()

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 700
        self.t = 0

    def update(self):
        v0 = 100
        alpha = 45 * (math.pi/180)
        g = 9.8
        x = v0 * math.cos(alpha) * self.t
        y = v0 * math.sin(alpha) * self.t - g * (self.t ** 2)/2
        self.rect.x = x + 100
        self.rect.y = 500 - y
        self.t += 0.1
        if self.t > (2 * v0 * math.sin(alpha))/g:
            self.t = 0


    def draw(self):
        self.screen.blit(self.image, self.rect)