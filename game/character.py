import os, pygame
from game import enums, globals
from game.bullet import Bullet


class Character(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.actions = enums.Action
        self.action = self.actions.idle
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.velocity_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.shooting = False
        self.playerState = {"moveLeft": False, "moveRight": False}
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.bullet_count = 100
        self.bullet_group = pygame.sprite.Group()
        self.score = 0
        self.animation_list = []
        
        animation_types = ['Idle', 'Run', 'Jump']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(os.path.join('assets', 'sprites', self.char_type, animation)))
            for i in range(num_of_frames):
                i = str(i)
                img = pygame.image.load(os.path.join('assets', 'sprites', self.char_type, animation, i+'.png')).convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)

            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action.value][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def shoot(self) :
        if self.bullet_count > 0:
            self.bullet_count = self.bullet_count - 1
            bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery,
                            self.direction)
            self.bullet_group.add(bullet)

    def update_score(self, increment):
        self.score = self.score + increment
       

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
        if self.jump and not self.in_air:
            self.velocity_y = -11
            self.jump = False
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

    def draw(self, screen):

        if self.alive:
            if self.shooting:
                self.shoot()
            if self.in_air:
                self.update_action(self.actions.jump)
            elif self.playerState["moveLeft"] or self.playerState["moveRight"]:
                self.update_action(self.actions.run)
            else:
                self.update_action(self.actions.idle)
            self.move(self.playerState["moveLeft"], self.playerState["moveRight"])

        self.bullet_group.update()
        self.bullet_group.draw(screen)
        print("Score: " + str(self.score))
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
