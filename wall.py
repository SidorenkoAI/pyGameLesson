import pygame
from pygame import Surface
import random
class Wall(pygame.sprite.Sprite):
    def __init__(self, screen: Surface):
        super().__init__()
        self.screen = screen
        self.orig_img = pygame.image.load('img/building.png')
        self.orig_img = pygame.transform.scale_by(surface=self.orig_img, factor=1.5)
        self.image = self.orig_img.copy()
        self.image.set_alpha(155)
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 400
        self.image_exp = pygame.image.load('img/exp2.png')
        self.rect_exp = self.image_exp.get_rect()
        self.sound = pygame.mixer.Sound('sound/vzryiv-vzorvavshegosya-snaryada.ogg')

    def collide(self, b):
        self.rect_exp = b.rect
        self.screen.blit(self.image_exp, self.rect_exp)
        self.sound.play()

    def draw(self):
        self.screen.blit(self.image, self.rect)