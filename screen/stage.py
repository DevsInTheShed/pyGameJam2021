from game.player import Player
import pygame 
from screen.screen import Screen
from level.level_1 import *
from game import globals

class Stage(Screen):
    def __init__(self, state):
        super().__init__(state)

             
        self.player1 = Player(globals.PlayerTypes["player"], 200, 200, 5)
        self.lvl1 = Level_1(self.player1)


    def draw(self):
        self.lvl1.draw()

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

