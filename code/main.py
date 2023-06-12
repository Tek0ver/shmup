import pygame
from settings import *
from sys import exit
from game import Game

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

gamedict = {
            'groups': {
                'player': pygame.sprite.GroupSingle(),
                'ennemies': pygame.sprite.GroupSingle(),
                'projectiles': pygame.sprite.Group(),
                'explosions': pygame.sprite.Group()
            }
        }

game = Game(gamedict)

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                gamedict['mixer'].toggle_music()
            elif event.key == pygame.K_k:
                gamedict['mixer'].change_music_volume('down')
            elif event.key == pygame.K_l:
                gamedict['mixer'].change_music_volume('up')

    screen.fill('grey')
    game.run(clock)
    pygame.display.update()

    clock.tick(FPS)
