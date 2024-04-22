import pygame
from pygame import Surface
import random
from Chel import Chel
class Gun(pygame.sprite.Sprite):
    def __init__(self, screen: Surface, pers: Chel):
        super().__init__()
        self.screen = screen

        self.pers = pers
        if self.pers.direction == 'up':
            self.direction = 'up'
            self.image = pygame.Surface((10, 50))
        elif self.pers.direction == 'down':
            self.direction = 'down'
            self.image = pygame.Surface((10, 50))
        elif self.pers.direction == 'left':
            self.direction = 'left'
            self.image = pygame.Surface((50, 10))
        elif self.pers.direction == 'right':
            self.direction = 'right'
            self.image = pygame.Surface((50, 10))
        self.rect = self.image.get_rect()
        self.rect.center = pers.rect.center
    def update(self):
        if self.direction == 'up':
            self.rect.y -= 1
        elif self.direction == 'down':
            self.rect.y += 1
        elif self.direction == 'left':
            self.rect.x -= 1
        elif self.direction == 'right':
            self.rect.x += 1
        if self.direction in ('up', 'down'):
            pygame.draw.rect(self.image, 'green', pygame.Rect(0, 0, 10, 50))
        else:
            pygame.draw.rect(self.image, 'green', pygame.Rect(0, 0, 50, 10))
