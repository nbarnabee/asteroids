import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)