import pygame
from coreSprite import CoreSprite


class Mine(CoreSprite):

    def __init__(self, pos):
        super().__init__()

        super().load_cache_images("../graphic/mine00")

        self.frame_index = 0
        self.animation_speed = 0.3

        self.image = self.images['mine00'][self.frame_index]
        self.rect = self.image.get_frect(center=pos)

    def update(self):

        self.animate()

    def animate(self):

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images['mine00']):
            self.frame_index = 0
        self.image = self.images['mine00'][int(self.frame_index)]
