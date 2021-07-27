from game.weapons import Weapon
import pygame
from game.character import Character
from game import globals
import random


class Enemy(Character):
    def __init__(self, char_type, x, y, speed, player):
        super().__init__(globals.EnemySprites[char_type], x, y, speed)
        self.player = player
        self.direction = random.choice([-1,1])
        self.moveCounter = 0
        self.idling = False
        self.idlingCounter = 0
        self.vision = pygame.Rect(0,0, 150, 20)
        
        laser = Weapon(ammo=-1, cooldown=80, damage=10)
        laser.active = True

        self.weapons = {
            "laser": laser
        }
        self.currentWeapon = "laser"
        self.enemies = [player]

    def brain(self):
        if self.alive == True:
            if random.randint(1, 200) == 1 and self.idling == False:
                self.idling = True
                self.idlingCounter = 50
                self.update_action(self.actions.idle)

            if  self.player.alive and self.vision.colliderect(self.player):
                self.update_action(self.actions.idle)
                self.shoot()
            else:
                if self.idling == False:
                    if self.direction == 1:
                        moveRight = True
                    else:
                        moveRight = False
                    moveLeft = not moveRight
                    self.move(moveLeft, moveRight)
                    self.update_action(self.actions.run)
                    self.moveCounter += 1

                    if self.moveCounter > globals.TileSize:
                        self.direction *= -1
                        self.moveCounter *= -1
                else:
                    self.idlingCounter -= 1
                    if self.idlingCounter <= 0:
                        self.idling = False

    def shoot(self) :
        if self.weapons[self.currentWeapon].timer == 0:
            self.weapons[self.currentWeapon].timer = self.weapons[self.currentWeapon].cooldown
            super().shoot()         
                    
    def update(self):
        if self.weapons[self.currentWeapon].timer > 0:
            self.weapons[self.currentWeapon].timer -= 1

    def draw(self):
        self.brain()
        self.update()

        health = globals.SmallFont.render(str(self.health), 1, globals.WHITE)
        text_width, text_height = globals.SmallFont.size(str(self.health))
        globals.ViewScreen.blit(health, (self.rect.centerx - text_width//2, self.rect.top - (text_height + 5)))
        self.vision.center = (self.rect.centerx + self.vision.width//2 * self.direction, self.rect.centery)
        super().draw()
