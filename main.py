import os, pygame
from game import globals
from game.gameState import GameState

pygame.init()
pygame.display.set_caption('Western Harry')

state = GameState()

while globals.GameRunning:
    globals.Clock.tick(globals.FPS)
    globals.GameRunning = state.render()
    pygame.display.update()

pygame.quit()
