import pygame
from pygame import Surface
class Chel:
    def __init__(self, path: str, screen: Surface):
        self.frames = self.getFrames(12, 4, path)
        self.down_frames = self.frames[:12]
        self.left_frames = self.frames[12:24]
        self.right_frames = self.frames[24:36]
        self.up_frames = self.frames[36:]
        self.frames = self.down_frames
        self.rectChel = self.frames[0].get_rect()
        self.rectChel.x = 0
        self.rectChel.y = 0
        self.index = 0

    def update(self, direction: str):
        if direction == 'up':


    def draw(self):
        pass

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
