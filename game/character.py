import os, pygame
from game import enums, globals
from game.bullet import Bullet


class Character(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.actions = enums.Action
        self.action = self.actions.idle
        self.alive = True
        self.speed = speed
        self.direction = 1
        self.velocity_y = 0
        self.in_air = True
        self.flip = False
        self.playerState = {
            pygame.K_LEFT: False, # Move Left 
            pygame.K_RIGHT: False, # Move Right 
            pygame.K_UP: False, # Jump
            pygame.K_SPACE: False # Shoot
        }
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.bullet_count = 100
        self.bullet_group = pygame.sprite.Group()
        self.animation_list = globals.CharacterSprites[char_type]
        self.image = self.animation_list[self.action.value][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def shoot(self) :
        if self.bullet_count > 0:
            self.bullet_count = self.bullet_count - 1
            bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery,
                            self.direction)
            self.bullet_group.add(bullet)       

    def move(self, move_left, move_right):
        delta_x = 0

        if move_left:
            delta_x = -self.speed
            self.flip = True
            self.direction = -1
        if move_right:
            delta_x = self.speed
            self.flip = False
            self.direction = 1
        if self.playerState[pygame.K_UP] and not self.in_air:
            self.velocity_y = -11
            self.playerState[pygame.K_UP] = False
            self.in_air = True

        self.velocity_y += globals.GRAVITY
        if self.velocity_y > 10:
            self.velocity_y = 10
        delta_y = self.velocity_y

        if self.rect.bottom + delta_y > 300:
            delta_y = 300 - self.rect.bottom
            self.in_air = False

        self.rect.x += delta_x
        self.rect.y += delta_y

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action.value][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action.value]):
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        self.update_animation()

        if self.alive:
            if self.playerState[pygame.K_SPACE]:
                self.shoot()
            if self.in_air:
                self.update_action(self.actions.jump)
            elif self.playerState[pygame.K_LEFT] or self.playerState[pygame.K_RIGHT]:
                self.update_action(self.actions.run)
            else:
                self.update_action(self.actions.idle)
            self.move(self.playerState[pygame.K_LEFT], self.playerState[pygame.K_RIGHT])

        self.bullet_group.update()
        self.bullet_group.draw(globals.ViewScreen)
        globals.ViewScreen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
