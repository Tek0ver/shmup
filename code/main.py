import pygame
from mixer import Mixer
from settings import *
from sys import exit
pygame.init()
from level import Level

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

modules = {
    'mixer': Mixer()
}

level = Level(modules)

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('grey')
    level.run()
    pygame.display.update()

    clock.tick(FPS)
