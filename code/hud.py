import pygame


class Hud:

    def __init__(self, screen: pygame.surface.Surface):
        
        self.screen = screen
        self.font = pygame.font.SysFont(None, 40)

    def display_text(self, pos, text: str):

        text_surf = self.font.render(text, True, 'white')
        self.screen.blit(text_surf, pos)
