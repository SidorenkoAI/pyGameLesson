import pygame

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


# pygame setup
pygame.init()
screen = pygame.display.set_mode((2000, 1200))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
running = True

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color = RED
bg = getBacground(screen, 100, 100, (0,0,0), (100,100,100))
radius = 0
while running:
    #screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, dest=(0, 0))
    pygame.draw.circle(screen,color=(124,50,100), center=screen.get_rect().center, radius=radius, width=5)
    radius += 1
    if radius > screen.get_width() // 2:
        radius = 0
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()