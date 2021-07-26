import os, pygame
from game.character import Character
from game import enums, globals
import random


class Enemy(Character):
    def __init__(self, char_type, x, y, speed):
        super().__init__(globals.EnemySprites[char_type], x, y, speed)
       

    def move(self):
        delta_x = 0

        move = random.randrange(0,10)

        if move > 4:
            super().move(True, False)
        else:
            super().move(False, True)


    

    # def update_action(self, new_action, bullet_group, player):
    #     if new_action != self.action:
    #         self.action = new_action
    #         self.frame_index = 0
    #         self.update_time = pygame.time.get_ticks()

    #     collisions = pygame.sprite.spritecollide(self, bullet_group, False)
    #     for bullet in collisions:
    #         bullet_group.remove(bullet)
    #         player.update_score(10)


    def draw(self):
        super().draw()
