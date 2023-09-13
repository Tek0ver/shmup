import pygame
from settings import *
from player import Player
from mixer import mixer


class Level:

    def __init__(self):

        self.groups = {
            'player': pygame.sprite.GroupSingle(),
            'ennemies': pygame.sprite.Group(),
            'projectiles': pygame.sprite.Group(),
        }

        self.config = {
            'lenght': 1000,
            'musics': {
                'main_music': '../audio/music/Juhani Junkala [Retro Game Music Pack] Level 1.wav',
            },
        }

        self.load_audio()

        mixer.toggle_music()

        self.spawn_player((50,50))

    def load_audio(self):
        
        for name, path in self.config['musics'].items():
            mixer.load_music(name, path)

    def spawn_player(self, pos):

        Player(self.groups, (50,50), 'blue', 3, 0.2, self.groups['player'])

    def run(self):

        self.groups['player'].update()
        self.draw()

    def draw(self):

        self.groups['player'].draw(pygame.display.get_surface())
