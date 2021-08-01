from game import enums
from game.globals import TileSize, TimeMachineList
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
            
            #weapons
            if self.itemType == enums.Collectable.ammo:
                self.player.weapons["shotgun"].bullet_count = self.player.weapons["shotgun"].maxAmmo
            if self.itemType == enums.Collectable.rocket:
                self.player.weapons["rocket"].bullet_count = self.player.weapons["rocket"].maxAmmo
            if self.itemType == enums.Collectable.fire:
                self.player.weapons["flamethrower"].bullet_count = self.player.weapons["flamethrower"].maxAmmo
            
            #player
            if self.itemType == enums.Collectable.health:
                self.player.health = self.player.max_health
            if self.itemType == enums.Objective.red or self.itemType == enums.Objective.green or self.itemType == enums.Objective.blue:
                self.player.objectives += 1
                self.player.collection.append(self.itemType)
            
            if self.itemType == enums.Collectable.jet:
                self.player.fuel = 100

        
class Decorators(Tile):
    def __init__(self, img, x ,y):
        super().__init__(img, x ,y)

class Water(Tile):
    def __init__(self, img, x ,y, player): 
        super().__init__(img, x ,y)
        self.player =player

    def update(self, scroll):
        super().update(scroll)

        if self.rect.collidepoint(self.player.rect.centerx,self.player.rect.bottom):
            self.player.health = 0


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.exitImages = TimeMachineList
        self.image = self.exitImages[enums.Objective.none.value]
        self.animation_list = [self.exitImages[4],self.exitImages[5]]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TileSize, y + (TileSize - self.image.get_height()))
        self.player = player

        #anim
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def update(self, scroll=0):
        self.rect.x += scroll

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        if enums.Objective.red in self.player.collection and \
        enums.Objective.green in self.player.collection and \
        enums.Objective.blue in self.player.collection: 
            self.image = self.animation_list[self.frame_index]
        else:
            self.image = self.exitImages[enums.Objective.none.value]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def draw(self, screen):
        self.update_animation()

        screen.blit(self.image, self.rect)
        if enums.Objective.red in self.player.collection: 
            screen.blit(self.exitImages[enums.Objective.red.value], self.rect)
        if enums.Objective.green in self.player.collection: 
            screen.blit(self.exitImages[enums.Objective.green.value], (self.rect.x, self.rect.y))
        if enums.Objective.blue in self.player.collection: 
            screen.blit(self.exitImages[enums.Objective.blue.value], self.rect)

    