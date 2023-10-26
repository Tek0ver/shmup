import pygame
from groupManager import groupManager

class Ui:

    def __init__(self):

        self.screen = pygame.display.get_surface()

        self.right_offset = self.screen.get_width() - 30
        self.left_offset = 30
        self.top_offset = 30
        self.bottom_offset = self.screen.get_height() - 30
        self.font = pygame.font.SysFont(None, 40)

    def draw(self, progress, score):

        player = groupManager.player.sprites()[0]

        life = player.life
        max_life = player.max_life
        shield = player.shield
        max_shield = player.max_shield

        # hp
        space = 30
        for i, bar in enumerate(range(max_life)):
            if i <= life:
                color = 'red'
            else:
                color = 'black'
            pygame.draw.ellipse(self.screen, color, (self.right_offset - i * space,20,20,40))

        # shield
        pygame.draw.line(self.screen, 'black', (self.right_offset + 20,75), (self.right_offset + 20 - max_shield * 1.4,75), 5)
        pygame.draw.line(self.screen, 'green', (self.right_offset + 20,75), (self.right_offset + 20 - shield * 1.4,75), 5)

        # progression
        pygame.draw.line(self.screen, 'black', (self.left_offset,self.bottom_offset), (self.left_offset,self.top_offset), 5)
        progress_y = self.bottom_offset - (self.bottom_offset - self.top_offset) * (progress / 100)
        pygame.draw.line(self.screen, 'blue', (self.left_offset,self.bottom_offset), (self.left_offset,progress_y), 5)

        # score
        img = self.font.render(f"{str(score)} points", True, 'black')
        self.screen.blit(img,
                         (self.right_offset - img.get_width(),
                          self.bottom_offset - img.get_height()))

        # speed

        # ammo

        # energy (laser, boost, shield ?)

ui = Ui()