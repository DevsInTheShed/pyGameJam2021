from game import enums
from game.globals import TileSize
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, img, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TileSize//2, y + (TileSize - self.image.get_height()))


    def update(self, scroll=0):
        self.rect.x += scroll

class WorldTile(Tile):
    def __init__(self, img, x ,y):
        super().__init__(img, x ,y)
        self.rect.x = x 
        self.rect.y = y 

class ItemBox(Tile):
    def __init__(self, img, x ,y):
        super().__init__(img, x ,y)
        
class Decorators(Tile):
    def __init__(self, img, x ,y):
        super().__init__(img, x ,y)

class Water(Tile):
    def __init__(self, img, x ,y): 
        super().__init__(img, x ,y)