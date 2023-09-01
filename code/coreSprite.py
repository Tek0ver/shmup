import pygame
from os import walk
from os.path import join


class CoreSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    @classmethod
    def load_cache_images(cls, folder):
        
        print(f"LOADIND {cls.__name__}")

        cls.images = {}

        for path, _folders, files in walk(folder):
            images = []
            for file in files:
                animation = path.split("/")[-1]
                images.append(pygame.image.load(join(path, file)).convert_alpha())
            cls.images[animation] = images
