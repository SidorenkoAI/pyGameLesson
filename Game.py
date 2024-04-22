import pygame as pg
import pygame.sprite
from pygame import Surface
import random
from Asteroid import Asteroid
from Eliksir import Eliksir
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

    def update(self):
        self.addAst()
        self.grAst.update()
        self.grAst.draw(self.screen)
        self.grKol.update()
        self.grKol.draw(self.screen)