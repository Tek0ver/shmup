import pygame
from player import Player

class Game:

    def __init__(self):
        
        self.screen = pygame.display.get_surface()

        self.gamedict = {
            'groups': {
                'player': pygame.sprite.GroupSingle(),
                'projectiles': pygame.sprite.Group()
            }
        }

        player = Player(self.gamedict)
        self.gamedict['groups']['player'].add(player)

    def run(self):
        
        self.gamedict['groups']['player'].update()
        self.gamedict['groups']['player'].draw(self.screen)

        self.gamedict['groups']['projectiles'].update()
        self.gamedict['groups']['projectiles'].draw(self.screen)
