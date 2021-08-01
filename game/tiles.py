from pygame import sprite
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
    def __init__(self, img, x ,y, itemType, player):
        super().__init__(img, x ,y)
        self.itemType = itemType
        self.player = player

    def update(self, scroll):
        super().update(scroll)

        if pygame.sprite.collide_rect(self, self.player):
            self.kill()
            if self.itemType == enums.Collectable.ammo:
                self.player.weapons["shotgun"].bullet_count = self.player.weapons["shotgun"].maxAmmo
            if self.itemType == enums.Collectable.rocket:
                self.player.weapons["rocket"].bullet_count = self.player.weapons["rocket"].maxAmmo
            if self.itemType == enums.Collectable.fire:
                self.player.weapons["flamethrower"].bullet_count = self.player.weapons["flamethrower"].maxAmmo
            if self.itemType == enums.Collectable.health:
                self.player.health = self.player.max_health

        
class Decorators(Tile):
    def __init__(self, img, x ,y):
        super().__init__(img, x ,y)

class Water(Tile):
    def __init__(self, img, x ,y): 
        super().__init__(img, x ,y)