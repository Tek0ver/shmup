import pygame
from player import Player
from mine import Mine
from groupManager import groupManager
from vfx import Explosion
from ui import ui

class Game:

    def __init__(self):

        self.screen = pygame.display.get_surface()

        self.score = 0

        Mine.load_cache_images("../graphic/mine00")
        Explosion.load_cache_images()

        self.spawn_player((250,400))

    def input(self):

        pass

    def update(self):

        groupManager.player.update()
        groupManager.ennemy.update(groupManager.player.sprites()[0])
        groupManager.projectile.update()
        groupManager.explosion.update()

        if not groupManager.ennemy:
            self.spawn_ennemy('mine', (100,100))

        self.check_collision()

    def draw(self):

        groupManager.projectile.draw(self.screen)
        groupManager.player.draw(self.screen)
        groupManager.ennemy.draw(self.screen)
        groupManager.explosion.draw(self.screen)
        ui.draw(50, self.score)

    def spawn_player(self, pos):

        # TODO : clean player  and ship code
        groupManager.player.add(Player(pos, 'red', 2, .5))

    def spawn_ennemy(self, type, pos):

        if type == 'mine':
            groupManager.ennemy.add(Mine(pos))
        else:
            print("Unknown ennemy type to spawn")

    def check_collision(self):

        if pygame.sprite.groupcollide(groupManager.projectile,
                                   groupManager.ennemy,
                                   True,
                                   True,
                                   ):
            self.score += 1
