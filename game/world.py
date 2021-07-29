
import pygame
from game.collectable import Decorators, ItemBox
from game.enemy import Enemy
from game.globals import CollideLeft, CollideRight, EnemyTypes, TileList, TileSize, ViewScreen
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
                        self.obstacles.add(WorldTile(tileImg, tileRect.x, tileRect.y, self.player))

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

    
    def draw(self):
        # for tile in self.obstacles:
        #     ViewScreen.blit(tile[0], tile[1])

        self.obstacles.update()
        self.obstacles.draw(ViewScreen)


        self.decorators.update()
        self.decorators.draw(ViewScreen)

        self.collectables.update()
        self.collectables.draw(ViewScreen)

        
        for enemy in self.enemies:
            enemy.draw()


class WorldTile(pygame.sprite.Sprite):
    def __init__(self, img, x ,y, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.player = player
    
    def update(self):
        feet = self.player.rect.bottom - TileSize

        #collide left
        if self.rect.collidepoint(self.player.rect.right - TileSize, feet):
            self.player.state[pygame.K_RIGHT] = False
            self.player.rect.x -= 1

        # collide right
        if self.rect.collidepoint(self.player.rect.left + TileSize, feet):
            self.player.state[pygame.K_LEFT] = False
            self.player.rect.x += 1

        # collide feet
        if self.rect.collidepoint(self.player.rect.centerx, self.player.rect.bottom):
            if self.player.velocity_y >= 0:
                self.player.velocity_y = 0
                self.player.in_air = False
                self.player.delta_y = self.rect.top

        # collide head
        if self.rect.collidepoint(self.player.rect.centerx, self.player.rect.top):
            if self.player.velocity_y < 0:
                self.player.velocity_y = 0
                self.player.delta_y = self.rect.bottom
        