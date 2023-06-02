import pygame
from os import walk


def load_sprite_asset(path):

    pass

def cut_spritesheet(path, sprite_dim, alpha_key='auto'):

    sprites = []
    
    if alpha_key == 'auto':
        spritesheet = pygame.image.load(path).convert()
        transColor = spritesheet.get_at((0,0))
        spritesheet.set_colorkey(transColor)
    elif not alpha_key:
        spritesheet = pygame.image.load(path).convert_alpha()

    width = spritesheet.get_width()
    height = spritesheet.get_height()

    for j in range(int(height/sprite_dim[1])):
        for i in range(int(width/sprite_dim[0])):
            sprites.append(spritesheet.subsurface(i*sprite_dim[0], j*sprite_dim[1], sprite_dim[0], sprite_dim[1]))

    print(len(sprites))

    return sprites
