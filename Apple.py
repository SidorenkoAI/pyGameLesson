import pygame
from pygame import Surface
import random
class Apple(pygame.sprite.Sprite):
    def __init__(self, screen: Surface):
        super().__init__()
        self.screen = screen
        self.orig_img = pygame.image.load('img/apple.png')
        scale = (50, 50)
        self.orig_img = pygame.transform.scale(surface=self.orig_img, size=scale)
        self.image = self.orig_img.copy()
        self.image.set_alpha(120)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, int(self.screen.get_width() - self.image.get_width()))
        self.rect.y = random.randint(int(self.screen.get_height() // 100 * 75), int(self.screen.get_height() // 100 * 95))
        self.sound = pygame.mixer.Sound('sound/inecraft_pick_u.ogg')
