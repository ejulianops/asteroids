from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__()

    def draw(self, screen):
        pygame.draw.circle(screen, x, y, radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)