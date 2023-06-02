import pygame
from settings import *


class Level:

    def __init__(self):

        self.background = pygame.image.load("../graphic/terrain/sea01.jpg").convert()
        self.background = pygame.transform.smoothscale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def display_background(self, screen: pygame.surface.Surface):

        screen.blit(self.background, (0,0))