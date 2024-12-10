import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    gameloop(screen, timer)


def gameloop(screen, timer, dt=0):
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the world
        player.update(dt)

        # Clear screen
        screen.fill("black")

        # Draw to the screen
        player.draw(screen)
        pygame.display.flip()

        # Check delta-time
        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
