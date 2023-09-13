import pygame
from settings import *
from mixer import mixer
from sys import exit
from level import Level

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

level = Level()

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('grey')
    level.run()
    pygame.display.update()

    clock.tick(FPS)
