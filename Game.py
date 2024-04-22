import pygame as pg
import pygame.sprite
from pygame import Surface
import random
from Asteroid import Asteroid
from Eliksir import Eliksir
from Gun import Gun
from Chel import Chel
from Apple import Apple
class Game:
    def __init__(self, path:str, screen: Surface, pers: Chel):
        self.path = path
        self.screen = screen
        self.expImg = pygame.image.load('img/exp2.png')
        self.expRect = self.expImg.get_rect()
        self.grAst = pygame.sprite.Group()
        self.grApp = pygame.sprite.Group()
        self.grBullet = pygame.sprite.Group()
        self.grKol = pygame.sprite.Group()
        self.last_update = pg.time.get_ticks()
        self.font = pygame.font.SysFont('arial', 50)
        self.gameOverText = self.font.render('YOU DIED', True, 'red')
        self.pers = pers
        self.level = 1
    def addAst(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 600:
            self.last_update = now
            self.grAst.add(Asteroid(path=self.path, screen=self.screen, speedDown=self.level))
            self.grKol.add(Eliksir(screen=self.screen))
    def bang(self, rect: pygame.Rect):
        self.expRect.center = rect.center
        self.screen.blit(self.expImg, self.expRect)

    def gameOver(self):
        self.screen.blit(self.gameOverText, self.screen.get_rect().center)
    def checkGround(self):
        for ast in self.grAst:
            if ast.rect.y > self.screen.get_height() - 300:
                self.expRect.center = ast.rect.center
                self.screen.blit(self.expImg, self.expRect)
                self.grAst.remove(ast)
    def addBullet(self):
        self.grBullet.add(Gun(screen=self.screen, pers=self.pers))

    def addApp(self, number:int):
        for k in range(number):
            self.grApp.add(Apple(self.screen))
    def levelUp(self):
        self.level += 1
        for ast in self.grAst:
            ast.speedDown += 20

    def printStat(self):
        LvlText = self.font.render(f'Level {self.level}', True, 'green')
        self.screen.blit(LvlText, (self.screen.get_height() - 5, 100))
    def update(self):
        if len(self.grApp) == 0:
            self.addApp(10)
            self.levelUp()
        self.addAst()
        self.checkGround()
        self.grAst.update()
        self.grAst.draw(self.screen)
        self.grKol.update()
        self.grKol.draw(self.screen)
        self.grBullet.update()
        self.grBullet.draw(self.screen)
        self.grApp.draw(self.screen)
        self.printStat()