import pygame
from ships import Ship

# Player(gamedict, (200,200), 'blue', 1.2, 1)


class Player(Ship):

    def __init__(self, gamedict, pos, color, speed, cooldown, *groups) -> None:
        super().__init__(gamedict, pos, color, speed, cooldown, *groups)

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
