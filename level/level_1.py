import pygame
from game.globals import *
from game.enemy import Enemy

class Level_1:
    def __init__(self, player):
        self.title = "Level 1"
        self.player = player
        self.enemy = Enemy(EnemyTypes["alien1"], 400, 200, 2, self.player)
        
        self.enemy.enemies = [self.player]
        self.player.enemies = [self.enemy]
       

    def draw(self):
        ViewScreen.fill(ViewScreenBackgroundColor)
        Title = TitleFont.render(self.title, 1, WHITE)
        ViewScreen.blit(Title, (SCREEN.left + 20, 20))
        
        pygame.draw.line(ViewScreen, GroundColor, (0, 300), (SCREEN.width, 300))

        self.player.draw()

        self.enemy.draw()
        

