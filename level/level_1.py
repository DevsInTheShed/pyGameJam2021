from game.button import Button
import pygame
from game import globals
from game.enemy import Enemy

class Level_1:
    def __init__(self, player):
        self.title = "Level 1"
        self.player = player
        self.enemies = [Enemy(globals.EnemyTypes["alien1"], 400, 200, 2, self.player),
                        Enemy(globals.EnemyTypes["alien1"], 400, 300, 2, self.player),
                        Enemy(globals.EnemyTypes["alien1"], 400, 400, 2, self.player)]
        self.player.enemies = self.enemies 
    
    def draw_bg(self):
        #background
        width = globals.sky_img.get_width()
        for x in range(5):
            globals.ViewScreen.blit(globals.sky_img, ((x * width) - globals.bg_scroll * 0.5, 0))
            globals.ViewScreen.blit(globals.mountain_img, ((x * width) - globals.bg_scroll * 0.6, globals.SCREEN.height - globals.mountain_img.get_height() - 300))
            globals.ViewScreen.blit(globals.pine1_img, ((x * width) - globals.bg_scroll * 0.7, globals.SCREEN.height - globals.pine1_img.get_height() - 150))
            globals.ViewScreen.blit(globals.pine2_img, ((x * width) - globals.bg_scroll * 0.8, globals.SCREEN.height - globals.pine2_img.get_height()))
            
    def draw(self):
        globals.ViewScreen.fill(globals.ViewScreenBackgroundColor)
        Title = globals.TitleFont.render(self.title, 1, globals.WHITE)
        globals.ViewScreen.blit(Title, (globals.SCREEN.left + 20, 20))       
        
        self.draw_bg()
        pygame.draw.line(globals.ViewScreen, globals.GroundColor, (0, 300), (globals.SCREEN.width, 300), 10)
        
        for enemy in self.enemies:
            enemy.draw()

        if self.player.alive:
            self.player.draw()
        else:
            if self.player.lives > 0:
                if Button(globals.ViewScreen, globals.SCREEN.centerx - globals.StartImg.get_rect().width//2, globals.SCREEN.centery, globals.StartImg).draw():
                    self.player.respawn()


        
        

