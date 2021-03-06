import pygame
from game.globals import GameRunning, Clock, FPS, GameTitle
from game.gameState import GameState

pygame.init()
pygame.display.set_caption(GameTitle)

state = GameState()

while GameRunning:
    Clock.tick(FPS)
    GameRunning = state.render()
    pygame.display.update()

pygame.quit()     