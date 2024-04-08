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


def getFrames(w: int, h: int, filename: str):
    image = pygame.image.load(filename).convert_alpha()
    width, height = image.get_size()
    w = width / w
    h = height / h
    row = 0
    frames = []
    for j in range(int(height / h)):
        for i in range(int(width / w)):
            frames.append(image.subsurface(pygame.Rect(i * w, row, w, h)))
        row += int(h)
    return frames



def chel():
    pygame.init()
    screen = pygame.display.set_mode((2000, 1200))
    pygame.display.set_caption('Chel')
    frames = getFrames(12, 4, 'img/chel.png')
    down_frames = frames[:12]
    left_frames = frames[12:24]
    right_frames = frames[24:36]
    up_frames = frames[36:]
    frames = down_frames
    index = 0
    clock = pygame.time.Clock()
    while True:
        screen.fill((24,113,147))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            frames = up_frames
            index = (index + 1) % len(frames)
        elif keys[pygame.K_DOWN]:
            frames = down_frames
            index = (index + 1) % len(frames)
        elif keys[pygame.K_LEFT]:
            frames = left_frames
            index = (index + 1) % len(frames)
        elif keys[pygame.K_RIGHT]:
            frames = right_frames
            index = (index + 1) % len(frames)

        screen.blit(frames[index], (100, 100))
        pygame.display.flip()
    clock.tick(60)

chel()
pygame.quit()