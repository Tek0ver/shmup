import pygame
from utility import cut_spritesheet


class Explosion(pygame.sprite.Sprite):

    def __init__(self, pos, *groups) -> None:
        super().__init__(*groups)

        self.sprites = cut_spritesheet("../graphic/vfx/explosion/explosionframes.png", (128,128))
        self.frame = 0
        self.animation_speed = 0.5
        self.image = self.sprites[self.frame]
        self.rect = self.image.get_frect(center=pos)

    def update(self):

        self.animate()

    def animate(self):

        self.frame += self.animation_speed

        if self.frame <= len(self.sprites) - 1:
            self.image = self.sprites[int(self.frame)]
        else:
            self.kill()
            del(self)
