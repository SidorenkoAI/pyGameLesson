import pygame
import random
from Fox import Fox
from Kolobok import Kolobok
from Chel import Chel
from Game import Game
import tkinter
from tkinter import ttk

resolution = [1600,1200]
def menu():
    window = tkinter.Tk()
    window.geometry("600x500+1000+500")
    def butClick(combobox):
        global resolution
        resolution = list(map(int, combobox.get().split('x')))
        window.quit()
    label1 = tkinter.Label(window, text='''Разрешение экрана''',
                      font=('Times New Roman', 24, 'bold')
                      )
    label1.pack()
    resolution = ["800x600", "1600x1200", "2000x1000"]
    combobox = ttk.Combobox(values=resolution)
    combobox.set(resolution[0])
    combobox.pack()
    but = tkinter.Button(window, text='Start', command=lambda: butClick(combobox))
    but.pack()
    window.mainloop()

def chel():
    pygame.init()
    bg = pygame.image.load('img/back.jpg')
    screen = pygame.display.set_mode(resolution)

    pygame.display.set_caption('Chel')
    chel = Chel(path='img/chel.png', screen=screen)
    clock = pygame.time.Clock()
    game = Game(path='img/asteroid.png', screen=screen, pers=chel)
    game.addApp(20)

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
        elif keys[pygame.K_SPACE]:
            game.addBullet()
        pygame.sprite.groupcollide(game.grAst, game.grBullet, True, True)
        s = pygame.sprite.spritecollideany(chel, game.grAst)
        if s:
            s.sound.play()
            game.grAst.remove(s)
            chel.hp -= 10
            game.bang(chel.rect)
            if chel.hp < 1:
                game.gameOver()
                pygame.display.flip()
                pygame.time.wait(2000)
                return
        w = pygame.sprite.spritecollideany(chel, game.grApp)
        if w:
            w.sound.play()
            game.grApp.remove(w)
            chel.hp += 10

        k = pygame.sprite.spritecollideany(chel, game.grKol)
        if k:
            game.grKol.remove(k)
            chel.hp += 10
        chel.draw()
        game.update()
        pygame.display.flip()
        clock.tick(60)

#menu()
chel()
pygame.quit()