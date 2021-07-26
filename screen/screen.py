import pygame
from game import globals

class Screen:
    def __init__(self, state):
        self.globals = globals
        self.state = state
        
    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

            if event.type == pygame.QUIT:
                return False

        return True