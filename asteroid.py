import pygame

from circleshape import CircleShape
from constants import ASTEROID_LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_SPEEDUP
from random import uniform


class Asteroid(CircleShape):

    def __init__(self, position, radius):
        super().__init__(position, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, ASTEROID_LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = uniform(20, 50)
            a1 = Asteroid(self.position, new_radius)
            a1.velocity = self.velocity.copy().rotate(random_angle) * ASTEROID_SPEEDUP
            a2 = Asteroid(self.position, new_radius)
            a2.velocity = self.velocity.copy().rotate(-random_angle) * ASTEROID_SPEEDUP
