import pygame
from pygame import Surface
import random
import math
class Ball(pygame.sprite.Sprite):
    def __init__(self, path: str, screen: Surface, gun):
        super().__init__()
        self.screen = screen
        self.orig_img = pygame.image.load(path)
        scale = (50, 50)
        self.orig_img = pygame.transform.scale(surface=self.orig_img, size=scale)
        self.image = self.orig_img.copy()

        self.rect = self.image.get_rect()
        self.x0 = gun.rect.right
        self.y0 = gun.rect.y
        self.t = 0
        self.angle = gun.angle
    def update(self):
        v0 = 100
        alpha = self.angle * (math.pi/180)
        g = 9.8
        x = v0 * math.cos(alpha) * self.t
        y = v0 * math.sin(alpha) * self.t - g * (self.t ** 2)/2
        self.rect.x = x + self.x0
        self.rect.y = self.y0 - y
        self.t += 0.1




    def draw(self):
        self.screen.blit(self.image, self.rect)