import pygame as pg
from pygame import Surface
import random
class Asteroid:
    def __init__(self, path: str, screen: Surface):
        self.orig_img = pg.image.load(path)
        self.rect = self.orig_img.get_rect()
        self.rect.x = 600
        self.rect.y = 0
        self.scr = screen
        self.angle = 0
        self.rot: Surface
        self.asterList = []
        self.last_update = pg.time.get_ticks()
    def rotate(self, ast):
        #ast = [orig_img, rect, angle, img]
        ast[2] = (ast[2] + ast[5]) % 360
        ast[3] = pg.transform.rotate(ast[0], angle=ast[2])
        old_center = ast[1].center
        ast[1] = ast[3].get_rect()
        ast[1].center = old_center
        # self.angle = (self.angle - 1) % 360
        # old_center = self.rect.center
        # self.rot = pg.transform.rotate(self.orig_img, angle=self.angle)
        # self.rect = self.rot.get_rect()
        # self.rect.center = old_center
    def add(self):
        scale = (random.randint(30, 200), random.randint(30, 200))
        orig_img = pg.transform.scale(surface=self.orig_img, size=scale)
        img = orig_img.copy()
        angle = random.randint(0,360)
        rect = orig_img.get_rect()
        rect.x = random.randint(0, self.scr.get_width())
        rect.y = 0
        speedDown = random.randint(1, 3)
        speedRotation = random.randint(1, 5)
        angleDown = random.randint(-5,5)
        self.asterList.append([orig_img, rect, angle, img, speedDown, speedRotation, angleDown])
    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 500:
            self.last_update = now
            self.add()
        for ast in self.asterList:
            self.rotate(ast)
            ast[1].y += ast[4]
            ast[1].x += ast[6]
            self.scr.blit(ast[3], ast[1])
            if ast[1].y > self.scr.get_height() or ast[1].x > self.scr.get_width():
                self.asterList.remove(ast)
        print(len(self.asterList))
