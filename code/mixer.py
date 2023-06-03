import pygame

class Mixer:

    def __init__(self):

        self.sounds = {}

    def load_sound(self, name, path):
        
        self.sounds[name] = pygame.mixer.Sound(path)

    def play_sound(self, name):

        self.sounds[name].play()
