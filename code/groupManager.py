import pygame


class GroupManager:

    def __init__(self):

        self.player = pygame.sprite.Group()
        self.ennemy = pygame.sprite.Group()
        self.projectile = pygame.sprite.Group()
        self.explosion = pygame.sprite.Group()

    def reset(self):

        self.__init__()


groupManager = GroupManager()
