from pygame.sprite import RenderUpdates
from game.weapons import Weapon
import pygame
from game.globals import BulletImg, FlameImg, FlamethrowerImg, PlayerSprites, RocketImg, SCREEN, ScrollThreashold,ShotgunImg, TileSize
from game.character import Character

class Player(Character):
    def __init__(self, char_type, x, y, speed):
        super().__init__(char_type, PlayerSprites[char_type], x, y, speed)    
        self.objectives = 0
        self.collection = []
        self.lives = 3
        self.fuel = 100
        
        flamethrower = Weapon(ammo=1000, cooldown=1, damage=2, img=FlamethrowerImg, ammoImg=FlameImg)
        flamethrower.active = True
        
        shotgun = Weapon(ammo=20, cooldown=10, damage=50, img=ShotgunImg, ammoImg=BulletImg)
        shotgun.active = True
        
        rocket = Weapon(ammo=3, cooldown=30, damage=75, img=RocketImg, ammoImg=BulletImg)
        rocket.active = True

        self.weapons = {
            "shotgun": shotgun,
            "flamethrower": flamethrower,
            "rocket": rocket
        }
        self.currentWeapon = "shotgun"
    
    
    def weapon_cycle(self, i):
        lst = list(self.weapons) 
        try: 
            res = lst[lst.index(i)+1]  
        except(ValueError,IndexError):
            res = lst[0]

        if self.weapons[str(res)].active:
            return str(res)
        else:
            return self.weapon_cycle(str(res))
        

    def weapon_next(self):
        self.currentWeapon = self.weapon_cycle(self.currentWeapon)
        print(self.currentWeapon)

    def shoot(self) :
            if self.weapons[self.currentWeapon].bullet_count > 0 and self.weapons[self.currentWeapon].timer == 0:
                self.weapons[self.currentWeapon].timer = self.weapons[self.currentWeapon].cooldown
                self.weapons[self.currentWeapon].decr()
                super().shoot()     

    def update(self):
        if self.weapons[self.currentWeapon].timer > 0:
            self.weapons[self.currentWeapon].timer -= 1

        super().update()
    
    def respawn(self):
        self.lives -= 1
        self.health = self.max_health
        self.direction = 1
        self.velocity_y = 0
        self.speed = self.maxSpeed
        self.rect.x -= (TileSize*2)
        self.rect.y -= 0
        self.in_air = True
        self.alive = True
        self.update_action(self.actions.jump)
        
    def move(self, move_left, move_right, scroll, length):
        super().move(move_left, move_right)

        if self.state[pygame.K_v] and self.fuel > 0 and self.rect.top >= 0:
            self.fuel -= .5
            self.velocity_y = -5
            self.in_air = True

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
            
            if self.state[pygame.K_SPACE]:
                self.update_action(self.actions.shoot)
                self.shoot()  
            
            if self.in_air and not (self.action == self.actions.fly):
                self.update_action(self.actions.jump)
            elif self.in_air and (self.action == self.actions.fly):
                self.update_action(self.actions.fly)
            elif self.state[pygame.K_LEFT] or self.state[pygame.K_RIGHT]:
                self.update_action(self.actions.run)
            else:
                self.update_action(self.actions.idle)
            screenScroll = self.move(self.state[pygame.K_LEFT], self.state[pygame.K_RIGHT], scroll, length)
            bgScroll = screenScroll

        super().draw()
        return screenScroll, bgScroll
