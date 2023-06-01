import pygame
from os import walk


def load_sprite_asset(path):

    pass

def cut_spritesheet(path, sprite_dim, alpha=False):

    if not alpha:
        spritesheet = pygame.image.load(path).convert()
    else:
        spritesheet = pygame.image.load(path).convert_alpha(alpha)

cut_spritesheet("../graphic/vfx/explosion/explosionframes.png", (128,128))