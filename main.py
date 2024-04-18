import pygame
import random
from Fox import Fox
from Kolobok import Kolobok
from Chel import Chel

from Asteroid import Asteroid
def chel():
    pygame.init()
    screen = pygame.display.set_mode((2000, 1200))

    pygame.display.set_caption('Chel')
    chel = Chel(path='img/chel.png', screen=screen)
    clock = pygame.time.Clock()

    asteroids = Asteroid(path='img/asteroid.png', screen=screen)
    last_update = pygame.time.get_ticks()
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

        chel.draw()
        asteroids.update()
        pygame.display.flip()
    clock.tick(60)

chel()
pygame.quit()