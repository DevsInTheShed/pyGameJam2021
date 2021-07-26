import pygame
from game.globals import *
from game.enemy import Enemy

class Level_1:
    def __init__(self, player):
        self.title = "Level 1"
        self.player = player
        self.enemies = [Enemy(EnemyTypes["alien1"], 400, 200, 2, self.player),
                        Enemy(EnemyTypes["alien1"], 400, 300, 2, self.player),
                        Enemy(EnemyTypes["alien1"], 400, 400, 2, self.player)]
        
        self.player.enemies = self.enemies 
       

    def draw(self):
        ViewScreen.fill(ViewScreenBackgroundColor)
        Title = TitleFont.render(self.title, 1, WHITE)
        ViewScreen.blit(Title, (SCREEN.left + 20, 20))
        
        pygame.draw.line(ViewScreen, GroundColor, (0, 300), (SCREEN.width, 300))

        self.player.draw()

        for enemy in self.enemies:
            enemy.draw()
        

