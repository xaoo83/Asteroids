import pygame
from asteroid import Asteroid
from shot import Shot
from constants import *
from logger import log_state
from player import Player
from asteroidfield import *
from logger import log_event
import sys


def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0.0

	# player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable,drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, drawable, updatable)

	asteroidfield = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True == True:
		log_state()
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
			     return
		screen.fill("black")
		updatable.update(dt)

		for object in asteroids:
		    if object.collides_with(player):
			    log_event("player_hit")
			    print("Game over!")
			    sys.exit()

		for object in asteroids:
		    for shot in shots:
			    if shot.collides_with(object):
				    log_event("asteroid_shot")
				    object.kill()
				    shot.kill()


		for object in drawable:
		    object.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
