from game.hud import Hud
from game.player import Player
import pygame 
from screen.screen import Screen
from level.level_1 import *
from game import globals

class Stage(Screen):
    def __init__(self, state):
        super().__init__(state)
  
        self.hud = Hud()   
        self.player1 = Player(globals.PlayerTypes["player"], 200, 200, 5)
        self.lvl1 = Level_1(self.player1)
        

    def update(self):
        self.hud.health = self.player1.health
        self.hud.weapon = self.player1.weapons[self.player1.currentWeapon]

    def draw(self):
        self.update()
        self.lvl1.draw()
        self.hud.draw()

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

