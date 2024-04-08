import pygame

class Kolobok:
    def __init__(self):
        self.image = pygame.image.load(f"img/kolobok.png")
        self.x = 0
        self.y = 200
        self.angle = 0
        self.rotation = self.image

    def update(self, screen):
        screen.blit(self.rotation, (self.x, self.y))

    def step_right(self, speed=1):
        self.angle = (self.angle - 1) % 360
        self.rotation = pygame.transform.rotate(self.image, angle=self.angle)
        self.x += speed
