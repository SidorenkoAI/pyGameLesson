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
        self.rect.x = 100
        self.rect.y = 600
        self.t = 0
        self.sound = pygame.mixer.Sound('sound/gromkiy-moschnyiy-vyistrel-pushki.ogg')
        self.angle = 45
        self.speed = 10
        self.x = 0

    def update(self):
        alpha = self.angle * (math.pi / 180)
        g = 9.8
        x = self.speed ** 2 * math.sin(2 * alpha) / g
        self.x = x + self.rect.right

    def changeSpeed(self):
        self.speed += 1
        if self.speed > 150:
            self.speed = 10
    def upper(self):
        if self.angle <= 80:
            self.angle += 10
        self.image = pygame.transform.rotate(self.orig_img, angle=self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
    def lower(self):
        if self.angle >= 10:
            self.angle -= 10
        self.image = pygame.transform.rotate(self.orig_img, angle=self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
    def draw(self):
        self.screen.blit(self.image, self.rect)
        r = self.speed * 1.7
        g = 255 - self.speed * 1.25
        b = 0
        color = (r, g, b)
        pygame.draw.rect(surface=self.screen,
                         rect=pygame.Rect(self.rect.x, self.rect.y - 50, self.speed, 20),
                         color=color)
        pygame.draw.circle(self.screen, color='red', center=(self.x, self.rect.y),
                           radius=20)
        # pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(25 + self.rect.x + self.x, self.rect.y - 2.5, 5, 10))
        # pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(25 + self.rect.x + self.x - 2.5, self.rect.y, 10, 5))