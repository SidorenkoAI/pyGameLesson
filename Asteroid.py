import pygame as pg
from pygame import Surface
class Asteroid:
    def __init__(self, path: str, screen: Surface):
        self.orig_img = pg.image.load(path)
        self.rect = self.orig_img.get_rect()
        self.rect.x = 600
        self.rect.y = 0
        self.scr = screen
        self.angle = 0
        self.rot: Surface

    def rotate(self):
        self.angle = (self.angle - 1) % 360
        old_center = self.rect.center
        self.rot = pg.transform.rotate(self.orig_img, angle=self.angle)
        self.rect = self.rot.get_rect()
        self.rect.center = old_center
    def update(self):
        #newScale = pg.transform.scale(surface=self.orig_img, size=(250, 200))
        self.rect.y += 5
        self.rect.x += -3
        self.scr.blit(self.rot, self.rect)

