import pygame
from code.settings import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

render_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

from code.mixer import mixer
from sys import exit
from code.game import Game

game = Game(render_surface)

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

    render_surface.fill('grey')

    # game.input()
    game.update()
    game.draw()

    upscaled_surface = pygame.transform.scale(render_surface, (screen.get_width(), screen.get_height()))

    screen.blit(upscaled_surface, (0,0))

    pygame.display.flip()

    clock.tick(FPS)
