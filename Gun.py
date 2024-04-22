import pygame
from pygame import Surface
import random
from Chel import Chel
class Gun(pygame.sprite.Sprite):
    def __init__(self, screen: Surface, pers: Chel):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('img/kolobok.png')
        self.rect = self.image.get_rect()
        self.rect.center = pers.rect.center



    def update(self):
        self.rect.x += 1