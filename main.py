import pygame
import random
from Fox import Fox
from Kolobok import Kolobok
def getBacground(screen, w: int, h: int, color1, color2):
    bg = pygame.Surface(screen.get_size())
    colors = (color1, color2)
    i = 0
    y = 0
    while y < bg.get_height():
        x = 0
        while x < bg.get_width():
            pygame.draw.rect(surface=bg, color=colors[i % 2], rect=pygame.Rect(x, y, w, h))
            x += w
            i += 1
        y += h
        i += 1
    return bg


def foxRun():
    pygame.init()
    screen = pygame.display.set_mode((2000, 1200))
    pygame.display.set_caption('Fox')
    clock = pygame.time.Clock()
    fox = Fox()
    kolobok = Kolobok()
    fox_frame_counter = 0
    while True:
        screen.fill((24,113,147))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        kolobok.step_right()
        kolobok.update(screen)

        fox_frame_counter += clock.tick(60)
        if fox_frame_counter > 100:
            fox_frame_counter = 0
            fox.step_right(speed=5)
        fox.update(screen)



        pygame.display.flip()


foxRun()
pygame.quit()