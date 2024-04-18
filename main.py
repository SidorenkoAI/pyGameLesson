import pygame
import random
from Fox import Fox
from Kolobok import Kolobok
from Chel import Chel

from Asteroid import Asteroid

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/kolobok.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 300)
        self.rect.y = random.randint(0, 300)
    def update(self):
        self.rect.x += 1
    def draw(self, screen):
        screen.blit(self.image, self.rect)


def chel():
    pygame.init()
    screen = pygame.display.set_mode((2000, 1200))

    pygame.display.set_caption('Chel')
    chel = Chel(path='img/chel.png', screen=screen)
    clock = pygame.time.Clock()
    kolGroup = pygame.sprite.Group()
    for i in range(10):
        kolGroup.add(Mob())
    asteroids = Asteroid(path='img/asteroid.png', screen=screen)
    while True:
        screen.fill((24,113,147))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            chel.update('up')

        elif keys[pygame.K_DOWN]:
            chel.update('down')

        elif keys[pygame.K_LEFT]:
            chel.update('left')

        elif keys[pygame.K_RIGHT]:
            chel.update('right')
        kolGroup.update()
        kolGroup.draw(screen)
        chel.draw()
        s = pygame.sprite.spritecollideany(chel, kolGroup)
        if s:
            kolGroup.remove(s)

        asteroids.update()
        pygame.display.flip()
    clock.tick(60)

chel()
pygame.quit()