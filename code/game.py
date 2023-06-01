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
        self.gamedict['groups']['ennemies'].update()

        self.gamedict['groups']['player'].draw(self.screen)
        self.gamedict['groups']['projectiles'].draw(self.screen)
        self.gamedict['groups']['ennemies'].draw(self.screen)

    def check_collisions(self):

        pass
