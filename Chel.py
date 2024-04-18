import random

import pygame
from pygame import Surface
class Chel(pygame.sprite.Sprite):
    def __init__(self, path: str, screen: Surface, speed = 5):
        super().__init__()
        self.screen = screen
        self.frames = self.getFrames(12, 4, path)
        self.down_frames = self.frames[:12]
        self.left_frames = self.frames[12:24]
        self.right_frames = self.frames[24:36]
        self.up_frames = self.frames[36:]
        self.frames = self.down_frames
        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect()
        self.rect.x = random.randint(0, self.screen.get_width())
        self.rect.y = random.randint(0, self.screen.get_height())
        self.index = 0
        self.speed = speed
        self.hp = 100

    def update(self, direction: str):
        if direction == 'up':
            self.frames = self.up_frames
            self.rect.y -= self.speed
        elif direction == 'down':
            self.frames = self.down_frames
            self.rect.y += self.speed
        elif direction == 'left':
            self.frames = self.left_frames
            self.rect.x -= self.speed
        elif direction == 'right':
            self.frames = self.right_frames
            self.rect.x += self.speed
        self.index = (self.index + 1) % len(self.frames)

    def draw(self):
        self.screen.blit(self.frames[self.index], self.rect)

    def getFrames(self, w: int, h: int, filename: str):
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
