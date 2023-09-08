import pygame
from settings import *
from player import Player
from mixer import Mixer


class Level:

    def __init__(self, modules):

        self.group_player = pygame.sprite.GroupSingle()
        self.group_ennemies = pygame.sprite.Group()

        self.config = {
            'lenght': 1000,
        }

        print(modules['mixer'].sounds)

    def run(self):

        pass

    def draw(self):

        pass
