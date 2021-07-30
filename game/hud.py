
import pygame
from game.globals import BLACK, HudChrome, RED, SCREEN, SmallFont, TitleFont, ViewScreen, WHITE


class Hud:
    def __init__(self):
        self.chromeImg = HudChrome
        self.rect = self.chromeImg.get_rect()
        self.rect.center = (SCREEN.centerx, SCREEN.bottom - HudChrome.get_height()//2)
        self.lives = None
        self.health = None     
        self.weapon = None
        self.fuel = 100
        
        self.space = 10
        self.healthBarWidth = 100
        self.weaponRect = pygame.Rect(self.rect.left+self.space, self.rect.top+self.space, 200, 300)        

    def draw(self):
        ViewScreen.blit(self.chromeImg, self.rect)
        
        healthBar = pygame.Rect(self.rect.right - (self.healthBarWidth+self.space), self.rect.top + self.space, self.healthBarWidth, self.health)
        healthBar.bottom = self.rect.bottom
        pygame.draw.rect(ViewScreen, BLACK, healthBar)

        health = SmallFont.render(str(self.health), 1, WHITE)
        text_width, text_height = SmallFont.size(str(self.health))
        ViewScreen.blit(health, (healthBar.centerx - text_width//2, healthBar.top - (text_height + 5)))

        lives = TitleFont.render(str(self.lives), 1, WHITE)
        text_width, text_height = TitleFont.size(str(self.lives))
        ViewScreen.blit(lives, (healthBar.centerx - text_width//2, healthBar.bottom - (text_height + 50)))

        ammoBar = pygame.Rect(self.rect.left + self.weaponRect.width + self.space, self.rect.top + self.space, self.weapon.bullet_count*4, 20)
        pygame.draw.rect(ViewScreen, BLACK, ammoBar)
        fuelBar = pygame.Rect(self.rect.left + self.weaponRect.width + self.space, self.rect.top + self.space*4, self.fuel*4, 20)
        pygame.draw.rect(ViewScreen, RED, fuelBar)

        ViewScreen.blit(self.weapon.image, self.weaponRect)
        