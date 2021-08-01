
import pygame
from game.tiles import Decorators, Exit, ItemBox, Water, WorldTile
from game.enemy import Enemy
from game.globals import EnemyTypes, TileList, TileSize, ViewScreen
from game import enums


class World():
    def __init__(self, player):
        self.player = player
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.collectables = pygame.sprite.Group()
        self.objectives = pygame.sprite.Group()
        self.decorators = pygame.sprite.Group()
        self.water = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
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
                    if tile >= 0 and tile <= 9:
                        self.obstacles.add(WorldTile(tileImg, tileRect.x, tileRect.y))

                    #tar
                    elif tile >=11 and tile <= 12:
                        self.water.add(Water(tileImg, tileRect.x, tileRect.y, self.player))  
                    
                    #decorators
                    elif tile >=13 and tile <= 18:
                        self.decorators.add(Decorators(tileImg, tileRect.x, tileRect.y)) 
                    
                    #ammo
                    elif tile == 19:
                        self.collectables.add(ItemBox(tileImg, tileRect.x, tileRect.y, enums.Collectable.ammo, self.player))

                    #rocket
                    elif tile == 20:
                        self.collectables.add(ItemBox(tileImg, tileRect.x, tileRect.y, enums.Collectable.rocket, self.player))
                    
                    #fire
                    elif tile == 21:
                        self.collectables.add(ItemBox(tileImg, tileRect.x, tileRect.y, enums.Collectable.fire, self.player))

                    #health
                    elif tile == 22:
                        self.collectables.add(ItemBox(tileImg, tileRect.x, tileRect.y, enums.Collectable.health, self.player))

                    #health
                    elif tile == 23:
                        self.collectables.add(ItemBox(tileImg, tileRect.x, tileRect.y, enums.Collectable.jet, self.player))

                    #green
                    elif tile == 24:
                        self.objectives.add(ItemBox(tileImg, tileRect.x, tileRect.y, enums.Objective.green, self.player))

                    #red
                    elif tile == 25:
                        self.objectives.add(ItemBox(tileImg, tileRect.x, tileRect.y, enums.Objective.red, self.player))

                    #blue
                    elif tile == 26:
                        self.objectives.add(ItemBox(tileImg, tileRect.x, tileRect.y, enums.Objective.blue, self.player))
                        
                     #enemies
                    elif tile == 27:
                        self.enemies.add(Enemy(EnemyTypes["alien1"], tileRect.x, tileRect.y+TileSize, 2, self.player))

                    #Exit
                    elif tile == 28:
                        self.exits.add(Exit(tileRect.x, tileRect.top, self.player))

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

        self.objectives.update(scroll)
        self.objectives.draw(ViewScreen)

        self.water.update(scroll)
        self.water.draw(ViewScreen)
        
        for enemy in self.enemies:
            enemy.draw(scroll)

        for exit in self.exits:
            exit.update(scroll)
            exit.draw(ViewScreen)



