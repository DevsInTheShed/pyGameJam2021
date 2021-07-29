import importlib
from game.hud import Hud
from game.player import Player
import pygame 
from screen.screen import Screen
from game import globals


class Stage(Screen):
    def __init__(self, state):
        super().__init__(state)
        self.gameState = state
        self.init = False
        self.player1 = Player(globals.PlayerTypes["player"], 205, 450, 5)        
        self.hud = Hud() 

    def levelInit(self):
        module = importlib.import_module(f'.level{self.gameState.currentLevel.value}', package='level')
        class_ = getattr(module, 'Level')
        self.lvl = class_(self.player1)

    def update(self):
        if not self.init:
            self.levelInit()
            self.init = True

        self.hud.lives = self.player1.lives
        self.hud.health = self.player1.health
        self.hud.weapon = self.player1.weapons[self.player1.currentWeapon]

    def draw(self):
        self.update()
        self.lvl.draw()
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

