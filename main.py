import os, pygame
from game.globals import *
from game.gameState import GameState

pygame.init()
pygame.display.set_caption('Western Defender')

state = GameState()

while GameRunning:
    Clock.tick(FPS)
    GameRunning = state.render()
    pygame.display.update()

pygame.quit()
