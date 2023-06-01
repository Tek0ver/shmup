import pygame
from player import Player
from ships import Ship

class Game:

    def __init__(self):
        
        self.screen = pygame.display.get_surface()

        self.gamedict = {
            'groups': {
                'player': pygame.sprite.GroupSingle(),
                'ennemies': pygame.sprite.GroupSingle(),
                'projectiles': pygame.sprite.Group()
            }
        }

        player = Player(self.gamedict, (200,200), 'blue', 1.2, 1)
        self.gamedict['groups']['player'].add(player)

        ennemy = Ship(self.gamedict, (50,50), 'red', 0.1, 2)
        self.gamedict['groups']['ennemies'].add(ennemy)

    def run(self):

        self.gamedict['groups']['player'].update()
        self.gamedict['groups']['projectiles'].update()

        self.check_collisions()

        self.gamedict['groups']['ennemies'].update()

        self.gamedict['groups']['projectiles'].draw(self.screen)
        self.gamedict['groups']['ennemies'].draw(self.screen)
        self.gamedict['groups']['player'].draw(self.screen)

    def spawn_ennemy(self):

        ennemy = Ship(self.gamedict, (50,50), 'red', 0.1, 2)
        self.gamedict['groups']['ennemies'].add(ennemy)

    def check_collisions(self):

        group_projectiles = self.gamedict['groups']['projectiles']
        group_ennemies = self.gamedict['groups']['ennemies']

        collided_dict = pygame.sprite.groupcollide(group_projectiles, group_ennemies, False, False)

        for projectile in collided_dict.keys():
            projectile.destroy()

        for l in collided_dict.values():
            for ennemy in l:
                ennemy.destroy()
                self.spawn_ennemy()
