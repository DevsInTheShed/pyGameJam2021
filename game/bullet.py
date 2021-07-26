import pygame
import os
from game.globals import *

class Bullet(pygame.sprite.Sprite):
	def __init__(self, owner, x, y, direction):
		pygame.sprite.Sprite.__init__(self)
		self.speed = 10
		self.damage = 5
		self.image = BulletImg
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.direction = direction
		self.owner = owner

	def update(self):
		#move bullet
		self.rect.x += (self.direction * self.speed)
		#check if bullet has gone off screen
		if self.rect.right < SCREEN.left or self.rect.left > SCREEN.right:
			self.kill()

		for enemy in self.owner.enemies:
			if pygame.sprite.spritecollide(enemy, self.owner.bullet_group, False):
				if enemy.alive:
						enemy.health -= self.damage
						self.kill()
						