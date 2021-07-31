from typing import Any
import pygame
from game import enums
from game.globals import GRAVITY, TileSize, ViewScreen
from game.bullet import Bullet


class Character(pygame.sprite.Sprite):
    def __init__(self, spriteArr, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.actions = enums.Action
        self.action = self.actions.idle
        self.alive = True
        self.health = 100
        self.max_health = self.health
        self.speed = speed
        self.maxSpeed = self.speed
        self.direction = 1
        self.velocity_y = 0
        self.in_air = True
        self.flipSprite = False
        self.state = {
            pygame.K_LEFT: False, # Move Left 
            pygame.K_RIGHT: False, # Move Right 
            pygame.K_UP: False, # Jump
            pygame.K_SPACE: False, # Shoot
            pygame.K_v: False #Tlue
        }

        self.weapons = {}
        self.currentWeapon = ""

        # Sprite Animation
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_list = spriteArr
        self.image = self.animation_list[self.action.value][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.floor = y

        # Bullets
        self.bullet_group = pygame.sprite.Group()

        # Enemy List
        self.enemies = []

    def move(self, move_left, move_right):
        self.delta_x = 0

        if move_left:
            self.delta_x = -self.speed
            self.flipSprite = True
            self.direction = -1
        if move_right:
            self.delta_x = self.speed
            self.flipSprite = False
            self.direction = 1
        if self.state[pygame.K_UP] and not self.in_air:
            self.velocity_y = -11
            self.state[pygame.K_UP] = False
            self.in_air = True
            
        
        self.velocity_y += GRAVITY
        if self.velocity_y > 10:
            self.velocity_y = 10
        delta_y = self.velocity_y
        
        if self.rect.bottom + delta_y > self.floor:
            delta_y = self.floor - self.rect.bottom
            self.in_air = False

        self.rect.x += self.delta_x
        self.rect.y += delta_y


    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action.value][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action.value]):
            if self.action == self.actions.death:
                self.frame_index = len(self.animation_list[self.action.value]) -1
            else:
                self.frame_index = 0

    def shoot(self):
        damage = self.weapons[self.currentWeapon].damage
        ammoImg = self.weapons[self.currentWeapon].ammoImg
        bullet = Bullet(ammoImg, self, self.rect.centerx + (0.75 * self.rect.width * self.direction), self.rect.centery, self.direction, damage)
        self.bullet_group.add(bullet) 
    
    def checkLife(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(self.action.death)


    def collision(self, obstacles):
        self.obstacles = obstacles
            
    
    def update(self):
        for block in self.obstacles:

            #collide left
            if self.rect.collidepoint(block.rect.left, block.rect.centery):
                self.state[pygame.K_RIGHT] = False
                self.rect.x -= 1

            # # collide right
            if self.rect.collidepoint(block.rect.right, block.rect.centery):
                self.state[pygame.K_LEFT] = False
                self.rect.x += 1

            # # collide feet
            if self.rect.collidepoint(block.rect.centerx, block.rect.top):
                if self.velocity_y >= 0:
                    self.velocity_y = 0
                    self.in_air = False
                    self.delta_y = block.rect.top

            # # collide head
            if self.rect.collidepoint(block.rect.centerx, block.rect.bottom):
                if self.velocity_y < 0:
                    self.velocity_y = 0
                    self.delta_y = block.rect.bottom


    
    def draw(self):
        self.update_animation()
        self.checkLife()

        self.bullet_group.update()
        self.bullet_group.draw(ViewScreen)
        
        ViewScreen.blit(pygame.transform.flip(self.image, self.flipSprite, False), self.rect)

