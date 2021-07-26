from game.weapons import Weapon
import pygame
from game import globals
from game.character import Character

class Player(Character):
    def __init__(self, char_type, x, y, speed):
        super().__init__(globals.PlayerSprites[char_type], x, y, speed)    
        shotgun = Weapon(100, 20)
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

    def draw(self):
        self.update()

        if self.alive:
            if self.state[pygame.K_SPACE]:
                self.shoot()
            if self.in_air:
                self.update_action(self.actions.jump)
            elif self.state[pygame.K_LEFT] or self.state[pygame.K_RIGHT]:
                self.update_action(self.actions.run)
            else:
                self.update_action(self.actions.idle)
            self.move(self.state[pygame.K_LEFT], self.state[pygame.K_RIGHT])

        super().draw()
