import pygame

class Kolobok(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load(f"img/kolobok.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 700
        self.screen = screen
        self.sound = pygame.mixer.Sound('sound/vzryiv-vzorvavshegosya-snaryada.ogg')

    def play(self):
        self.sound.play()
    def draw(self):
        self.screen.blit(self.image, self.rect)


