import os, pygame
from game import globals
from game.character import Character, enums
from game.screen.stage import Stage
from game.gameState import GameState

pygame.init()
pygame.display.set_caption('Western Harry')

state = GameState(globals)

while globals.GameRunning:
    globals.Clock.tick(globals.FPS)
    globals.GameRunning = state.render()
    pygame.display.update()

pygame.quit()
