import pygame as pg
import pygame.sprite
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
        self.image = pg.transform.rotate(self.orig_img, angle=self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedDown
        self.rect.x += self.angleDown

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
        self.angle = (self.angle + self.speedRotation) % 360
        self.image = pg.transform.rotate(self.orig_img, angle=self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedDown
        self.rect.x += self.angleDown

class Game:
    def __init__(self, path:str, screen: Surface):
        self.path = path
        self.screen = screen
        self.expImg = pygame.image.load('img/exp2.png')
        self.expRect = self.expImg.get_rect()
        self.grAst = pygame.sprite.Group()
        self.grKol = pygame.sprite.Group()
        self.last_update = pg.time.get_ticks()
        self.font = pygame.font.SysFont('arial', 50)
        self.gameOverText = self.font.render('YOU DIED', True, 'red')
    def addAst(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 600:
            self.last_update = now
            self.grAst.add(Asteroid(path=self.path, screen=self.screen))
            self.grKol.add(Eliksir(screen=self.screen))
    def bang(self, rect: pygame.Rect):
        self.expRect.center = rect.center
        self.screen.blit(self.expImg, self.expRect)

    def gameOver(self):
        self.screen.blit(self.gameOverText, self.screen.get_rect().center)


