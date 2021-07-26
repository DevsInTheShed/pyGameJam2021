import os, pygame
from game import enums, globals
from game.bullet import Bullet
from game.character import Character


class Player(Character):
    def __init__(self, char_type, x, y, speed):
        super().__init__(globals.PlayerSprites[char_type], x, y, speed)    
        self.bullet_count = 100

    def shoot(self) :
        if self.bullet_count > 0:
            self.bullet_count = self.bullet_count - 1
            super().shoot()     


    def draw(self):
        
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
