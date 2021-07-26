import pygame 
from screen.screen import Screen
from level.level_1 import *

class Stage(Screen):
    def __init__(self, state, player1):
        super().__init__(state)
        self.player1 = player1
        
        self.lvl1 = Level_1(self.state.update_score)

    def draw(self):
        self.lvl1.draw()
        self.player1.draw()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                else:
                    self.player1.state[event.key] = True

            if event.type == pygame.KEYUP:
                self.player1.state[event.key] = False

            if event.type == pygame.QUIT:
                return False

        return super().draw()

