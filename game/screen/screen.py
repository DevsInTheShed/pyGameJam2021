import pygame

class Screen:
    def __init__(self, globals):
        self.globals = globals

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

            if event.type == pygame.QUIT:
                return False

        return True