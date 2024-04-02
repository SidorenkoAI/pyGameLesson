import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
running = True
screen.fill("white")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color = RED
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            color = BLUE
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            color = GREEN

    # fill the screen with a color to wipe away anything from last frame
    pygame.draw.rect(surface=screen, color=color, rect=pygame.Rect(400, 300, 400, 300), width=5)
    pygame.draw.line(surface=screen, color=color, start_pos=(400, 300), end_pos=(600, 200), width=5)
    pygame.draw.line(surface=screen, color=color, start_pos=(600, 200), end_pos=(800, 300), width=5)
    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()