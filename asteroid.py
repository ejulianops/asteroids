import pygame 
import random 
from constants import * 
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_SHOOT_SPEED, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, dt, screen):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector_1 = pygame.Vector2(self.velocity).rotate(random_angle)
            vector_2 = pygame.Vector2(self.velocity).rotate(-random_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
            new_asteroid_1.update(dt)
            new_asteroid_1.draw(screen)
            new_asteroid_1.velocity = vector_1 * 1.2

            new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
            new_asteroid_2.update(dt)
            new_asteroid_2.draw(screen)
            new_asteroid_2.velocity = vector_2 * 1.2




#forward = pygame.Vector2(0, 1).rotate(self.rotation)