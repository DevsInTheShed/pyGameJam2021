import pygame
from game.globals import *
from game.enemy import Enemy

class Level_1:
    def __init__(self, update_score):
        self.title = "Level 1"
        self.enemy = Enemy('alien1', 400, 200, 3, 5, GRAVITY)
        self.update_score = update_score

    def draw(self):
        ViewScreen.fill(ViewScreenBackgroundColor)
        Title = TitleFont.render(self.title, 1, WHITE)
        ViewScreen.blit(Title, (SCREEN.left + 20, 20))
        
        pygame.draw.line(ViewScreen, GroundColor, (0, 300), (SCREEN.width, 300))

        self.enemy.update_animation()
        self.enemy.draw(ViewScreen)
        self.enemy.move()

