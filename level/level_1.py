import pygame
from game.globals import *

class Level_1:
    def __init__(self):
        self.title = "Level 1"

    def draw(self):
        ViewScreen.fill(ViewScreenBackgroundColor)
        Title = TitleFont.render(self.title, 1, WHITE)
        ViewScreen.blit(Title, (SCREEN.left + 20, 20))
        
        pygame.draw.line(ViewScreen, GroundColor, (0, 300), (SCREEN.width, 300))

