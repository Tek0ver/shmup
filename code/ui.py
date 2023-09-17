import pygame

class Ui:

    def __init__(self):

        pass

    def draw(self, life=2, shield=100):

        screen = pygame.display.get_surface()

        start_pos = screen.get_width() - 30

        # hp
        space = 30
        for i, bar in enumerate(range(5)):
            if i <= life:
                color = 'red'
            else:
                color = 'black'
            pygame.draw.ellipse(screen, color, (start_pos - i * space,20,20,40))

        # shield
        pygame.draw.line(screen, 'blue', (start_pos + 20,75), (start_pos + 20 - shield * 1.4,75), 5)

        # progression

        # score

ui = Ui()