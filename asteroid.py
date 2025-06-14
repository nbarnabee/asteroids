import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.position.x, self.position.y, new_radius)
            child2 = Asteroid(self.position.x, self.position.y, new_radius)
            child1.velocity = v1 * 1.2
            child2.velocity = v2 * 1.2
