import pygame as pg
import pygame.sprite
from pygame import Surface
import random
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, path: str, screen: Surface):
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
        self.speedDown = random.randint(1, 3)
        self.speedRotation = random.randint(1, 5)
        self.angleDown = random.randint(-5, 5)

    def rotate(self):
        #ast = [orig_img, rect, angle, img]
        self.angle = (self.angle + self.speedRotation) % 360
        self.image = pg.transform.rotate(self.orig_img, angle=self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        # self.angle = (self.angle - 1) % 360
        # old_center = self.rect.center
        # self.rot = pg.transform.rotate(self.orig_img, angle=self.angle)
        # self.rect = self.rot.get_rect()
        # self.rect.center = old_center
    # def add(self):
    #     scale = (random.randint(30, 200), random.randint(30, 200))
    #     orig_img = pg.transform.scale(surface=self.orig_img, size=scale)
    #     img = orig_img.copy()
    #     angle = random.randint(0,360)
    #     rect = orig_img.get_rect()
    #     rect.x = random.randint(0, self.scr.get_width())
    #     rect.y = 0
    #     speedDown = random.randint(1, 3)
    #     speedRotation = random.randint(1, 5)
    #     angleDown = random.randint(-5,5)
    #     self.asterList.append([orig_img, rect, angle, img, speedDown, speedRotation, angleDown])
    def update(self):
        self.rotate()
        self.rect.y += self.speedDown
        self.rect.x += self.angleDown
        # now = pg.time.get_ticks()
        # if now - self.last_update > 200:
        #     self.last_update = now
        #     self.add()
        # for ast in self.asterList:
        #     self.rotate(ast)
        #     ast[1].y += ast[4]
        #     ast[1].x += ast[6]
        #     self.scr.blit(ast[3], ast[1])
        #     if ast[1].y > self.scr.get_height() or ast[1].x > self.scr.get_width():
        #         self.astCounter += 1
        #         self.asterList.remove(ast)
        # self.printStat()


class Game:
    def __init__(self, path:str, screen: Surface):
        self.path = path
        self.screen = screen
        self.grAst = pygame.sprite.Group()
        self.last_update = pg.time.get_ticks()
    def addAst(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 200:
            self.last_update = now
            self.grAst.add(Asteroid(path=self.path, screen=self.screen))