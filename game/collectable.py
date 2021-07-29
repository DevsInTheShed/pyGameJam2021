from game import enums
from game.globals import TileSize
import pygame


class Collectable(pygame.sprite.Sprite):
    def __init__(self, img, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TileSize//2, y + (TileSize - self.image.get_height()))


    def update(self, scroll=0):
        self.rect.x += scroll

class ItemBox(Collectable):
    def __init__(self, img, x ,y):
        super().__init__(img, x ,y)
        
class Decorators(Collectable):
    def __init__(self, img, x ,y):
        super().__init__(img, x ,y)
