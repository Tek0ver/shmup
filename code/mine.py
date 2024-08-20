import pygame
from .coreSprite import CoreSprite, Destroyable
from .ai import AI_0


class Mine(CoreSprite, Destroyable, AI_0):

    def __init__(self, pos):
        CoreSprite.__init__(self)
        AI_0.__init__(self)

        self.frame_index = 0
        self.animation_speed = 0.3

        self.image = self.images['mine00'][self.frame_index]
        self.rect = self.image.get_frect(center=pos)

    def update(self, player):

        self.animate()
        self.get_movement(player)
        self.move()

    def animate(self):

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images['mine00']):
            self.frame_index = 0
        self.image = self.images['mine00'][int(self.frame_index)]
