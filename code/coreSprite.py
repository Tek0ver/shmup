import pygame
from os import walk
from os.path import join
import vfx
from groupManager import groupManager
from mixer import mixer


class CoreSprite(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

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


class Destroyable(pygame.sprite.Sprite):

    def kill(self):

        vfx.Explosion(self.rect.center, groupManager.explosion)
        # self.gamedict['mixer'].play_sound('dead')
        super().kill()
        