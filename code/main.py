import pygame
from settings import *
from mixer import mixer
from sys import exit

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

from level import Level

level = Level()

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

            elif event.key == pygame.K_a:
                level.spawn_ennemy((250,250), 0)

    screen.fill('grey')
    level.run()
    level.draw()
    pygame.display.flip()

    clock.tick(FPS)
