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

    return sprites


def load_image(path, alpha=True):

    if alpha:
        return pygame.image.load(path).convert_alpha()


def sorting_key(value):

    ls = value.split(".")
    return int(ls[0])


def load_image_folder(path):

    images = {}

    for folder_path, folder_in, files in walk(path):
        if files:
            animation = []
            files = sorted(files, key=sorting_key)
            for img in files:
                img_path = str(folder_path) + '/' + img
                animation.append(load_image(img_path))
            images[folder_path.split('/')[-1]] = animation

    return(images)
