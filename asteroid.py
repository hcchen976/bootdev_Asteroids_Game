import random

import pygame

import constants
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=constants.LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event(event_type="asteroid_split")
            split_angle = random.uniform(20, 50)
            new_asteroid_velocity_1 = self.velocity.rotate(split_angle)
            new_asteroid_velocity_2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
            new_asteroid_2 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)

            new_asteroid_1.velocity = new_asteroid_velocity_1 * 1.2
            new_asteroid_2.velocity = new_asteroid_velocity_2 * 1.2

