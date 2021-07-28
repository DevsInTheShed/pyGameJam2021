
from game.enemy import Enemy
from game.globals import EnemyTypes, TileList, TileSize, ViewScreen


class World():
    def __init__(self, player):
        self.player = player
        self.enemies = []
        self.obstacles = []
    
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
                        self.obstacles.append(tileData)

                    #water
                    elif tile >=9 and tile <= 10:
                        pass 
                    
                    #decorators
                    elif tile >=11 and tile <= 14:
                        pass 
                    
                    #enemies
                    elif tile == 15:
                        self.enemies.append(Enemy(EnemyTypes["alien1"], tileRect.x, tileRect.y+TileSize, 2, self.player))

                    #ammo
                    elif tile == 16:
                        pass

                    #granade
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
        for tile in self.obstacles:
            ViewScreen.blit(tile[0], tile[1])
        
        for enemy in self.enemies:
            enemy.draw()