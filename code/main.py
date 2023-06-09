import pygame
from settings import *
from sys import exit
from game import Game

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game = Game()

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('grey')
    game.run(clock)
    pygame.display.update()

    clock.tick(FPS)
