from game import enums
from game.globals import TileSize
import pygame


class ItemBox(pygame.sprite.Sprite):
    def __init__(self, img, x ,y):
        pygame.sprite.Sprite.__init__(self)
        #self.itemType = itemType
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TileSize//2, y + (TileSize - self.image.get_height()))



class Decorators(pygame.sprite.Sprite):
    def __init__(self, img, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TileSize//2, y + (TileSize - self.image.get_height()))
