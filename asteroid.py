import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		rock = pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		elif self.radius > ASTEROID_MIN_RADIUS:
			spread = random.uniform(20, 50)
			vel1 = self.velocity.rotate(spread)
			vel2 = self.velocity.rotate(-(spread))
			new_rad = (self.radius - ASTEROID_MIN_RADIUS)
			rock1 = Asteroid(self.position.x, self.position.y, new_rad)
			rock1.velocity = (vel1 * 1.2)
			rock2 = Asteroid(self.position.x, self.position.y, new_rad)
			rock2.velocity = (vel2 * 1.2)
