import pygame
from pygame import Surface
import random
class Eliksir(pygame.sprite.Sprite):
    def __init__(self, screen: Surface):
        super().__init__()
        self.screen = screen
        self.orig_img = pygame.image.load('img/kolobok.png')
        self.image = self.orig_img.copy()
        self.rect = self.image.get_rect()
        self.angle = random.randint(0, 360)
        self.rect.x = random.randint(0, self.screen.get_width())
        self.rect.y = 0
        self.speedDown = random.randint(1, 3)
        self.speedRotation = random.randint(1, 5)
        self.angleDown = random.randint(-5, 5)

    def rotate(self):
        self.angle = (self.angle + self.speedRotation) % 360
        self.image = pygame.transform.rotate(self.orig_img, angle=self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedDown
        self.rect.x += self.angleDown