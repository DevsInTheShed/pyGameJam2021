from pygame.sprite import RenderUpdates
from game.weapons import Weapon
import pygame
from game.globals import PlayerSprites, SCREEN, ScrollThreashold,ShotgunImg, TileSize
from game.character import Character

class Player(Character):
    def __init__(self, char_type, x, y, speed):
        super().__init__(PlayerSprites[char_type], x, y, speed)    
        self.lives = 3
        self.fuel = 100
        
        shotgun = Weapon(ammo=100, cooldown=20, damage=25, img=ShotgunImg)
        shotgun.active = True

        self.weapons = {
            "shotgun": shotgun
        }
        self.currentWeapon = "shotgun"

    def shoot(self) :
            if self.weapons[self.currentWeapon].bullet_count > 0 and self.weapons[self.currentWeapon].timer == 0:
                self.weapons[self.currentWeapon].timer = self.weapons[self.currentWeapon].cooldown
                self.weapons[self.currentWeapon].decr()
                super().shoot()     

    def update(self):
        if self.weapons[self.currentWeapon].timer > 0:
            self.weapons[self.currentWeapon].timer -= 1
    
    def respawn(self):
        self.lives -= 1
        self.health = self.max_health
        self.direction = 1
        self.velocity_y = 0.
        self.speed = self.maxSpeed
        self.in_air = True
        self.alive = True
        self.update_action(self.actions.jump)
        
    def move(self, move_left, move_right, scroll, length):
        super().move(move_left, move_right)

        if self.state[pygame.K_v] and self.fuel > 0:
            self.fuel -= .5
            self.velocity_y = -5

        #handle screen scroll on player
        if (self.rect.right > SCREEN.width - ScrollThreashold and scroll < (length * TileSize) - SCREEN.width) \
            or (self.rect.left < ScrollThreashold and scroll > abs(self.delta_x)):
            self.rect.x -= self.delta_x
            return -self.delta_x
        else:
            return 0

    def draw(self, scroll, length):
        self.update()
        
        if self.alive:
            if self.state[pygame.K_v]:
                self.update_action(self.actions.fly)
            if self.state[pygame.K_SPACE]:
                self.update_action(self.actions.shoot)
                self.shoot()  
            
            elif self.in_air:
                self.update_action(self.actions.jump)
            elif self.state[pygame.K_LEFT] or self.state[pygame.K_RIGHT]:
                self.update_action(self.actions.run)
            else:
                self.update_action(self.actions.idle)
            screenScroll = self.move(self.state[pygame.K_LEFT], self.state[pygame.K_RIGHT], scroll, length)
            bgScroll = screenScroll

        super().draw()
        return screenScroll, bgScroll
