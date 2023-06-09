import pygame
from player import Player
from ships import Ship
from level import Level
from hud import Hud
from settings import *
from mixer import Mixer


class Game:

    def __init__(self, gamedict):
        
        self.screen = pygame.display.get_surface()

        self.gamedict = gamedict

        self.level = Level()
        self.hud = Hud(self.screen)
        self.mixer = Mixer()
        self.gamedict['mixer'] = self.mixer

        self.mixer.load_music('main_00', '../audio/music/Juhani Junkala [Retro Game Music Pack] Level 1.wav')
        self.mixer.switch_music('main_00')
        self.mixer.toggle_music()

        self.score = 0

        player = Player(self.gamedict, (200,200), 'blue', 3, 1)
        self.gamedict['groups']['player'].add(player)

        ennemy = Ship(self.gamedict, (50,50), 'red', 0.1, 2)
        self.gamedict['groups']['ennemies'].add(ennemy)

    def run(self, clock):        

        self.gamedict['groups']['player'].update()
        self.gamedict['groups']['projectiles'].update()

        self.check_collisions()

        self.gamedict['groups']['ennemies'].update()
        self.gamedict['groups']['explosions'].update()

        self.level.display_background(self.screen)
        self.gamedict['groups']['projectiles'].draw(self.screen)
        self.gamedict['groups']['ennemies'].draw(self.screen)
        self.gamedict['groups']['player'].draw(self.screen)
        self.gamedict['groups']['explosions'].draw(self.screen)

        self.hud.display_text((50,WINDOW_HEIGHT - 50), f"Score : {self.score}")
        self.hud.display_fps(clock)

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
                self.score += 10
                self.spawn_ennemy()
