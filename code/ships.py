import pygame
from .timer import Timer
from .projectile import Projectile
from .vfx import Explosion
from .mixer import mixer
from .groupManager import groupManager


class Ship(pygame.sprite.Sprite):

    def __init__(self, pos, color, speed, cooldown, *groups) -> None:
        super().__init__(*groups)

        self.image = pygame.surface.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_frect(center=pos)

        self.direction = pygame.math.Vector2()
        self.speed = speed

        self.timer_shoot = Timer(cooldown)
        
        mixer.load_sound('shoot', 'audio/weapon/laser1.wav')
        mixer.load_sound('dead', 'audio/explosion/explosion.wav')
    
    def update(self) -> None:
        
        self.get_movement(groupManager.player.sprite)
        self.move()

    def move(self):

        if self.direction.magnitude() != 0:
            self.direction.normalize_ip()
        self.rect.center = self.rect.center + self.direction * self.speed

    def shoot(self, dir=1):
        
        if self.timer_shoot.trigger():
            mixer.play_sound('shoot')
            Projectile(self.rect.center, dir * 1, 10, groupManager.projectile)

    def get_movement(self, target):

        self.direction.x = target.rect.center[0] - self.rect.center[0]
        self.direction.y = target.rect.center[1] - self.rect.center[1]        

    def destroy(self):

        Explosion(self.rect.center, groupManager.explosion)
        mixer.play_sound('dead')
        self.kill()
        del(self)
