import pygame
from constants import *
from player import *
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)
def main():
	pygame.init
	fps = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	ship = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	while  1 == 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		updatable.update(dt)
		for things in drawable:
			things.draw(screen)
		pygame.display.flip()
		fps.tick(60)
		dt = (fps.get_time())/1000
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()
