import pygame

class GroupManager:

    def __init__(self):

        self.player = pygame.sprite.Group()
        self.ennemy = pygame.sprite.Group()
        self.projectile = pygame.sprite.Group()
        self.explosion = pygame.sprite.Group()


groupManager = GroupManager()
