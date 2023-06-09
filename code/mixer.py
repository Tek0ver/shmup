import pygame

class Mixer:

    def __init__(self):

        self.sounds = {}
        self.musics = {}
        self.active_music = ''
        self.music_state = 'off'

    def load_sound(self, name, path):
        
        self.sounds[name] = pygame.mixer.Sound(path)

    def load_music(self, name, path):

        self.musics[name] = pygame.mixer.music.load(path)

    def play_sound(self, name):
        self.sounds[name].play()

    def toggle_music(self):
                
        if self.music_state is 'off':
            pygame.mixer.music.play(-1)
            self.music_state = 'playing'
        elif self.music_state is 'playing':
            pygame.mixer.music.pause()
            self.music_state = 'paused'
        elif self.music_state is 'paused':
            pygame.mixer.music.unpause()
            self.music_state = 'playing'


    def switch_music(self, music: str):
        
        self.active_music = music