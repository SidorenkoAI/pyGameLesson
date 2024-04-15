import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):

    def __init__(self, screen):

        #load image
        super(Raindrop, self).__init__()
        self.screen = screen
        self.pic = pygame.image.load('rain.png')
        self.image = pygame.transform.smoothscale(self.pic,(50,60))
        self.rect = self.image.get_rect()

        #starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blit(self):
        for raindrop_number in range(raindrop_number_x):
            raindrop = Raindrop(screen)
            raindrop.rect.x = raindrop.rect.x + 2 * raindrop.rect.x * raindrop_number  # use loop variable
            raindrops.add(raindrop)