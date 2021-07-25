import pygame
import os
from game.globals import *

class Bullet(pygame.sprite.Sprite):

	def __init__(self, x, y, direction):
		pygame.sprite.Sprite.__init__(self)
		self.speed = 10
		path = os.path.join('assets', 'sprites', 'icons')
		self.image = pygame.image.load(path + '/bullet.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.direction = direction

	def update(self, enemy, bullet_group):
		#move bullet
		self.rect.x += (self.direction * self.speed)
		#check if bullet has gone off screen
		if self.rect.right < 0 or self.rect.left > SCREEN.width:
			self.kill()