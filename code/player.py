import pygame
from ships import Ship
from utility import *


class Player(Ship):

    def __init__(self, all_groups, pos, color, speed, cooldown, *groups) -> None:
        super().__init__(all_groups, pos, color, speed, cooldown, *groups)

        self.frames = load_image_folder('../graphic/ship00')['ship00']
        self.idle_frame = len(self.frames) / 2
        self.frame_index = int(self.idle_frame)

        self.status = 'idle'

        self.turning_animation_speed = 0.4

        print(self.frame_index)

        self.image = self.frames[int(self.frame_index)]
        self.rect = self.image.get_frect(center=pos)

        self.keys = {
            'up': pygame.K_UP,
            'down': pygame.K_DOWN,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'shoot': pygame.K_SPACE
            }

    def update(self) -> None:
        
        self.get_input()
        self.move()
        self.get_status()
        self.animate()

    def get_status(self):

        if self.direction.x < 0:
            self.status = 'left'
        elif self.direction.x > 0:
            self.status = 'right'
        else:
            self.status = 'idle'

    def animate(self):

        if self.status in ['left']:
            self.frame_index -= self.turning_animation_speed
            if self.frame_index <= 0:
                self.frame_index = 0
        elif self.status in ['right']:
            self.frame_index += self.turning_animation_speed
            if self.frame_index >= len(self.frames):
                self.frame_index = int(self.frame_index) - 1
        else:
            if self.frame_index >= self.idle_frame:
                self.frame_index -= self.turning_animation_speed
            elif self.frame_index <= self.idle_frame:
                self.frame_index += self.turning_animation_speed
        
        self.image = self.frames[int(self.frame_index)]

    def get_input(self):

        keys = pygame.key.get_pressed()
        
        if keys[self.keys['up']]:
            self.direction.y = -1
        elif keys[self.keys['down']]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[self.keys['left']]:
            self.direction.x = -1
        elif keys[self.keys['right']]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
        if keys[self.keys['shoot']]:
            self.shoot(-1)
