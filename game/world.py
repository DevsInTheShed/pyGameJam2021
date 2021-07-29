
from game.player import Player
import pygame
from game.collectable import Decorators, ItemBox
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
    
    def processData(self, data):
        # iterate through level data
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
                        pass 
                    
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

        return self.enemies

    def collision(self, blocklist, character):
        for block in blocklist:
            feet = character.rect.bottom - TileSize

            #collide left
            if block.rect.collidepoint(character.rect.right - TileSize, feet):
                character.state[pygame.K_RIGHT] = False
                character.rect.x -= 1

            # collide right
            if block.rect.collidepoint(character.rect.left + TileSize, feet):
                character.state[pygame.K_LEFT] = False
                character.rect.x += 1

            # collide feet
            if block.rect.collidepoint(character.rect.centerx, character.rect.bottom):
                if character.velocity_y >= 0:
                    character.velocity_y = 0
                    character.in_air = False
                    character.delta_y = block.rect.top

            # collide head
            if block.rect.collidepoint(character.rect.centerx, character.rect.top):
                if character.velocity_y < 0:
                    character.velocity_y = 0
                    character.delta_y = block.rect.bottom


    def update(self):
        feet = self.player.rect.bottom - TileSize

        self.collision(self.obstacles, self.player)

        for enemy in self.enemies:
            self.collision(self.obstacles, enemy)

        
    def draw(self, scroll=0):
        self.update()

        self.obstacles.update(scroll)
        self.obstacles.draw(ViewScreen)


        self.decorators.update(scroll)
        self.decorators.draw(ViewScreen)

        self.collectables.update(scroll)
        self.collectables.draw(ViewScreen)

        
        for enemy in self.enemies:
            enemy.draw(scroll)


class WorldTile(pygame.sprite.Sprite):
    def __init__(self, img, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

    def update(self, scroll=0):
        self.rect.x += scroll
