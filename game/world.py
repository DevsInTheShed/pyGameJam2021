
from game.player import Player
import pygame
from game.tiles import Decorators, ItemBox, Water, WorldTile
from game.enemy import Enemy
from game.globals import EnemyTypes, TileList, TileSize, ViewScreen
from game import enums


class World():
    def __init__(self, player):
        self.player = player
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.collectables = pygame.sprite.Group()
        self.decorators = pygame.sprite.Group()
        self.water = pygame.sprite.Group()
        self.length = 0
    
    def processData(self, data):
        # iterate through level data
        self.length = len(data[0])
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    tileImg = TileList[tile]
                    tileRect = tileImg.get_rect()
                    tileRect.x = x * TileSize
                    tileRect.y = y * TileSize
                    tileData = (tileImg, tileRect)

                    #obstacles
                    if tile >= 0 and tile <= 8:
                        self.obstacles.add(WorldTile(tileImg, tileRect.x, tileRect.y))

                    #water
                    elif tile >=9 and tile <= 10:
                        self.water.add(Water(tileImg, tileRect.x, tileRect.y))  
                    
                    #decorators
                    elif tile >=11 and tile <= 14:
                        self.decorators.add(Decorators(tileImg, tileRect.x, tileRect.y)) 
                    
                    #enemies
                    elif tile == 15:
                        self.enemies.add(Enemy(EnemyTypes["alien1"], tileRect.x, tileRect.y+TileSize, 2, self.player))

                    #ammo
                    elif tile == 16:
                        self.collectables.add(ItemBox(tileImg, tileRect.x, tileRect.y))

                    #weapon
                    elif tile == 17:
                        pass
                    
                    #health
                    elif tile == 18:
                        pass

                    #exit
                    elif tile == 19:
                        pass

        self.player.collision(self.obstacles)
        for enemy in self.enemies:
            enemy.collision(self.obstacles)
        
        return self.enemies

 
    def draw(self, scroll=0):

        self.obstacles.update(scroll)
        self.obstacles.draw(ViewScreen)

        self.decorators.update(scroll)
        self.decorators.draw(ViewScreen)

        self.collectables.update(scroll)
        self.collectables.draw(ViewScreen)

        self.water.update(scroll)
        self.water.draw(ViewScreen)
        
        for enemy in self.enemies:
            enemy.draw(scroll)



