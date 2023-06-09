import pygame

class Mixer:

    def __init__(self):

        self.sounds = {}
        self.musics = {}

    def load_sound(self, name, path):
        
        self.sounds[name] = pygame.mixer.Sound(path)

    def load_music(self, name, path):

        self.musics[name] = pygame.mixer.music()

    def play_sound(self, name):

        self.sounds[name].play()
