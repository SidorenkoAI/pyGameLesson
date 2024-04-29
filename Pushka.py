import pygame
from pygame import Surface
import random
import math
class Pushka(pygame.sprite.Sprite):
    def __init__(self, path: str, screen: Surface):
        super().__init__()
        self.screen = screen
        self.orig_img = pygame.image.load(path)
        self.orig_img = pygame.transform.scale_by(surface=self.orig_img, factor=0.5)
        self.image = self.orig_img.copy()
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 500
        self.t = 0
        self.sound = pygame.mixer.Sound('sound/gromkiy-moschnyiy-vyistrel-pushki.ogg')



    def draw(self):
        self.screen.blit(self.image, self.rect)