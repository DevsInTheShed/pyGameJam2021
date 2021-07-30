import pygame
from game.globals import BulletImg, SCREEN

class Bullet(pygame.sprite.Sprite):
	def __init__(self, ammoImg, owner, x, y, direction, damage):
		pygame.sprite.Sprite.__init__(self)
		self.speed = 10
		self.damage = damage
		self.image = ammoImg
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

		if self.owner.currentWeapon == "flamethrower":
			if self.owner.direction == 1 and self.rect.x >= (self.owner.rect.x + 200):
				self.kill()
			if self.owner.direction == -1 and self.rect.x <= (self.owner.rect.x - 200):
				self.kill()

		for enemy in self.owner.enemies:
			if pygame.sprite.spritecollide(enemy, self.owner.bullet_group, False):
				if enemy.alive:
						enemy.health -= self.damage
						self.kill()
						