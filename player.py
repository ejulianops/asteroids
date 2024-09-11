import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    
    def __init__(self, x, y):        
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # To draw the player, override the draw method of CircleShape. 
    # It should take the screen object as a parameter, and call pygame.draw.polygon
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # assignment: Add a new method to the Player class called rotate. 
    # It's going to take one argument: dt. 
    # When it's called, it should add PLAYER_TURN_SPEED * dt to the player's current rotation.
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_w]:
            self.move(dt)
        self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, shots_group):
        if self.timer <= 0:
            velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            new_shot = Shot(self.position, velocity)
            shots_group.add(new_shot)
            self.timer = PLAYER_SHOOT_COOLDOWN 
