import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    gameloop(surface, timer)


def gameloop(surface, timer, dt=0):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw stuff

        # Call pygame.display.flip()

        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
