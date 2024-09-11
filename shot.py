import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED

# Create a new Shot class to represent a bullet. 
# It should also inherit from CircleShape so that it can use our collision detection code. 
# Use a new SHOT_RADIUS constant and set it to 5.
class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, radius=SHOT_RADIUS)
        self.velocity = velocity

    # Create the image
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        
        # Create the rect
        self.rect = self.image.get_rect(center=position)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position