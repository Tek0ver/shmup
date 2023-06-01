import pygame
from projectile import Projectile
from timer import Timer


class Player(pygame.sprite.Sprite):

    def __init__(self, gamedict, *groups) -> None:
        super().__init__(*groups)

        self.gamedict = gamedict

        spawn_point = (200, 200)

        self.direction = pygame.math.Vector2()
        self.speed = 1.2

        self.image = pygame.surface.Surface((10,20))
        self.image.fill('blue')
        self.rect = self.image.get_frect(center=spawn_point)

        self.timer_shoot = Timer(2)

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
            self.shoot()

    def move(self):
        
        self.rect.center = self.rect.center + self.direction * self.speed

    def shoot(self):
        
        if self.timer_shoot.trigger():
            Projectile(self.rect.center, -1, 2, self.gamedict['groups']['projectiles'])
