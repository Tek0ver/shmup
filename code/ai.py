import pygame

class AI_0:

    def __init__(self):

        self.direction = pygame.math.Vector2()
        self.speed = 1

    def get_movement(self, target):

        self.direction.x = target.rect.center[0] - self.rect.center[0]
        self.direction.y = target.rect.center[1] - self.rect.center[1]

    def move(self):

        if self.direction.magnitude() != 0:
            self.direction.normalize_ip()
        self.rect.center = self.rect.center + self.direction * self.speed
