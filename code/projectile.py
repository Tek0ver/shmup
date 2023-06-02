import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, pos, dir, speed, *groups) -> None:
        super().__init__(*groups)

        self.dir = dir
        self.speed = speed

        self.image = pygame.image.load("../graphic/vfx/weapon/laser-00.png").convert_alpha()
        self.rect = self.image.get_frect(center=pos)

    def update(self):
        
        self.move()

    def move(self):

        self.rect.y = self.rect.y + self.dir * self.speed

        if self.rect.bottom <= -10:
            self.kill()
            del(self)

    def destroy(self):

        self.kill()
        del(self)
