from game.button import Button
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
    
    def draw_bg(self):
        #background
        width = sky_img.get_width()
        for x in range(5):
            ViewScreen.blit(sky_img, ((x * width) - bg_scroll * 0.5, 0))
            ViewScreen.blit(mountain_img, ((x * width) - bg_scroll * 0.6, SCREEN.height - mountain_img.get_height() - 300))
            ViewScreen.blit(pine1_img, ((x * width) - bg_scroll * 0.7, SCREEN.height - pine1_img.get_height() - 150))
            ViewScreen.blit(pine2_img, ((x * width) - bg_scroll * 0.8, SCREEN.height - pine2_img.get_height()))
            
    def draw(self):
        ViewScreen.fill(ViewScreenBackgroundColor)
        Title = TitleFont.render(self.title, 1, WHITE)
        ViewScreen.blit(Title, (SCREEN.left + 20, 20))       
        
        self.draw_bg()
        pygame.draw.line(ViewScreen, GroundColor, (0, 300), (SCREEN.width, 300), 10)
        
        for enemy in self.enemies:
            enemy.draw()

        if self.player.alive:
            self.player.draw()
        else:
            if self.player.lives > 0:
                if Button(ViewScreen, SCREEN.centerx - StartImg.get_rect().width//2, SCREEN.centery, StartImg).draw():
                    self.player.respawn()


        
        

