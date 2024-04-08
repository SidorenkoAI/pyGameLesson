import pygame

class Fox:
    def __init__(self):
        self.frames = list()
        for i in range(1, 9):
            self.frames.append(pygame.image.load(f"img/fox{i}.png"))

        self.img = self.frames[0]
        self.index = 0
        self.x = 0
        self.y = 0

    def update(self, screen):
        screen.blit(self.img, (self.x, self.y))
    def step_right(self, speed = 1):
        self.index += 1
        if self.index >= len(self.frames):
            self.index = 0
        self.img = self.frames[self.index]
        self.x += speed

