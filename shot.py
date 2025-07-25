from constants import *
from circleshape import *

class Shot(CircleShape):
	def __init__(self, x, y, velocity):
		super().__init__(x, y, SHOT_RADIUS)
		self.velocity = velocity

	def draw(self, screen):
		bullet = pygame.draw.circle(screen, "white", self.position, self.radius)

	def update(self, dt):
		self.position += (self.velocity * dt)

