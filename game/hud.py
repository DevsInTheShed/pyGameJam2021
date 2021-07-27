
import pygame
from game.globals import BLACK, HudChrome, SCREEN, SmallFont, ViewScreen, WHITE


class Hud:
    def __init__(self):
        self.chromeImg = HudChrome
        self.rect = self.chromeImg.get_rect()
        self.rect.center = (SCREEN.centerx, SCREEN.bottom - HudChrome.get_height()//2)
        width, height = self.chromeImg.get_width(), self.chromeImg.get_height()
        self.health = any      
        # self.weapon = any

        self.space = 20
        self.healthBarWidth = 100
        
        # self.weaponRect = self.weapon.image.get_rect()
        # self.weaponRect.rect.center = (SCREEN.centerx, SCREEN.centery)
        

    def draw(self):
        ViewScreen.blit(self.chromeImg, self.rect)
        
        healthBar = pygame.Rect(self.rect.right - (self.healthBarWidth+self.space), self.rect.top + self.space, self.healthBarWidth, self.health)
        healthBar.bottom = self.rect.bottom
        pygame.draw.rect(ViewScreen, BLACK, healthBar)

        health = SmallFont.render(str(self.health), 1, WHITE)
        text_width, text_height = SmallFont.size(str(self.health))
        ViewScreen.blit(health, (healthBar.centerx - text_width//2, healthBar.top - (text_height + 5)))

        ammoBar = pygame.Rect(self.rect.left + 200, self.rect.top +20, self.weapon.bullet_count*4, 20)
        pygame.draw.rect(ViewScreen, BLACK, ammoBar)

        # ViewScreen.blit(self.weapon.image, self.weaponRect)
        