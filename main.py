import pygame
import random
from Fox import Fox
from Kolobok import Kolobok
from Chel import Chel
from Game import Game

def chel():
    pygame.init()
    bg = pygame.image.load('img/back.jpg')
    screen = pygame.display.set_mode(bg.get_size())

    pygame.display.set_caption('Chel')
    chel = Chel(path='img/chel.png', screen=screen)
    clock = pygame.time.Clock()
    game = Game(path='img/asteroid.png', screen=screen)

    while True:
        screen.blit(bg, (0,0))
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
        s = pygame.sprite.spritecollideany(chel, game.grAst)
        if s:
            game.grAst.remove(s)
            chel.hp -= 10
            game.bang(chel.rect)
            if chel.hp < 1:
                game.gameOver()
                pygame.display.flip()
                pygame.time.wait(2000)
                return
        k = pygame.sprite.spritecollideany(chel, game.grKol)
        if k:
            game.grKol.remove(k)
            chel.hp += 10
        chel.draw()
        game.update()
        pygame.display.flip()
        clock.tick(60)

chel()
pygame.quit()