import pygame
from constants import *
from circleshape import *
from shot import *


class Player(CircleShape):
	def __init__(self, x, y, shot_group, updatable_group, drawable_group):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shots = shot_group
		self.updatable = updatable_group
		self.drawable = drawable_group
		self.cooldown = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		ship = pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED * dt)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		bullet = Shot(self.position.x, self.position.y, ((pygame.Vector2(0,1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED))
		self.shots.add(bullet)
		self.updatable.add(bullet)
		self.drawable.add(bullet)
		self.cooldown =  PLAYER_SHOOT_COOLDOWN

	def update(self, dt):
		keys = pygame.key.get_pressed()
		self.cooldown -= dt

		if keys[pygame.K_a]:
			self.rotate(-(dt))

		if keys[pygame.K_d]:
			self.rotate(dt)

		if keys[pygame.K_s]:
			self.move(-(dt))

		if keys[pygame.K_w]:
			self.move(dt)

		if keys[pygame.K_SPACE]:
			if self.cooldown > 0:
				return
			else:
				self.shoot()

