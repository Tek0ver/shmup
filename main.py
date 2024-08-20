import pygame
from code.settings import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

from code.mixer import mixer
from sys import exit
from code.game import Game

game = Game()

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                mixer.toggle_music()
            elif event.key == pygame.K_k:
                mixer.change_music_volume('down')
            elif event.key == pygame.K_l:
                mixer.change_music_volume('up')

    screen.fill('grey')

    # game.input()
    game.update()
    game.draw()
    
    pygame.display.flip()

    clock.tick(FPS)
