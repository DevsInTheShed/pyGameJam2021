import pygame 
from screen.screen import Screen
from level.level_1 import *

class Stage(Screen):
    def __init__(self, state, player1):
        super().__init__(state)
        self.player1 = player1
        self.playerState = {
            "player1": {"moveLeft": False, "moveRight": False}
        }
        
        self.lvl1 = Level_1()

    def draw(self):
        self.lvl1.draw()

        self.player1.update_animation()
        self.player1.draw(self.globals.ViewScreen)


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_LEFT:
                    self.player1.playerState["moveLeft"] = True
                if event.key == pygame.K_RIGHT:
                    self.player1.playerState["moveRight"] = True
                if event.key == pygame.K_UP and self.player1.alive:
                    self.player1.jump = True
                if event.key == pygame.K_SPACE:
                    self.player1.shooting = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player1.playerState["moveLeft"] = False
                if event.key == pygame.K_RIGHT:
                    self.player1.playerState["moveRight"] = False
                if event.key == pygame.K_UP and self.player1.alive:
                    self.player1.jump = False
                if event.key == pygame.K_SPACE:
                    self.player1.shooting = False
            
            if event.type == pygame.QUIT:
                return False
        
        return super().draw()

