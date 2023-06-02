from typing import Any
import pygame
from timer import Timer
from projectile import Projectile
from vfx import Explosion


class Ship(pygame.sprite.Sprite):

    def __init__(self, gamedict, pos, color, speed, cooldown, *groups) -> None:
        super().__init__(*groups)

        self.gamedict = gamedict

        self.image = pygame.surface.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_frect(center=pos)

        self.direction = pygame.math.Vector2()
        self.speed = speed

        self.timer_shoot = Timer(cooldown)
    
    def update(self) -> None:
        
        self.get_movement(self.gamedict['groups']['player'].sprite)
        self.move()

    def move(self):
        
        self.rect.center = self.rect.center + self.direction * self.speed

    def shoot(self):
        
        if self.timer_shoot.trigger():
            Projectile(self.rect.center, -1, 2, self.gamedict['groups']['projectiles'])

    def get_movement(self, target):

        self.direction.x = target.rect.x - self.rect.x
        self.direction.y = target.rect.y - self.rect.y
        if self.direction.magnitude != 0:
            self.direction.normalize_ip()

    def destroy(self):

        Explosion(self.rect.center, self.gamedict['groups']['explosions'])
        self.kill()
        del(self)
