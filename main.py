import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    gameloop(
        screen,
        timer,
        {"updatable": updatable, "drawable": drawable, "asteriods": asteroids},
    )


def gameloop(screen, timer, groups):
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the world
        for obj in groups["updatable"]:
            obj.update(dt)

        # Clear screen
        screen.fill("black")

        # Draw to the screen
        for obj in groups["drawable"]:
            obj.draw(screen)

        pygame.display.flip()

        # Check delta-time
        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
