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

    def change_music_volume(self, volume: str) -> float:

        step = 0.1

        if volume == 'up':
            actual_volume = pygame.mixer.music.get_volume() + step
            if actual_volume > 1:
                actual_volume = 1
        elif volume == 'down':
            actual_volume = pygame.mixer.music.get_volume() - step
            if actual_volume < 0:
                actual_volume = 0
        
        pygame.mixer.music.set_volume(actual_volume)

        print(f"Volume set to {actual_volume}.")

        return actual_volume