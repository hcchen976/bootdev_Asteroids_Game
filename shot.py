import pygame

import constants
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius=constants.SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=constants.SHOT_RADIUS)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt