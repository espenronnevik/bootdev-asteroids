import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    containers = []

    def __init__(self, position, radius):
        # we will be using this later
        super().__init__(self.containers)

        self.position = pygame.Vector2.copy(position)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, circleobj):
        return self.position.distance_to(circleobj.position) < (
            self.radius + circleobj.radius
        )
