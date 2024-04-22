import pygame as pg
import pygame.sprite
from pygame import Surface
import random



class Asteroid(pygame.sprite.Sprite):
    def __init__(self, path: str, screen: Surface, speedDown):
        super().__init__()
        self.orig_img = pg.image.load(path)
        self.screen = screen
        scale = (random.randint(30, 200), random.randint(30, 200))
        self.orig_img = pg.transform.scale(surface=self.orig_img, size=scale)
        self.image = self.orig_img.copy()
        self.rect = self.image.get_rect()
        self.angle = random.randint(0, 360)
        self.rect.x = random.randint(0, self.screen.get_width())
        self.rect.y = 0
        self.speedDown = random.randint(speedDown, speedDown + 2)
        self.speedRotation = random.randint(1, 5)
        self.angleDown = random.randint(-5, 5)

    def rotate(self):
        self.angle = (self.angle + self.speedRotation) % 360
        self.image = pg.transform.rotate(self.orig_img, angle=self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedDown
        self.rect.x += self.angleDown



