# assignment 1: import pygame at the top of your main.py file.
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
from constants import PLAYER_SHOOT_SPEED

# assignment 3: Ensure our predefined constants imported at the top of your file
from constants import *

def main():

    # assignment 2: Initialize pygame at the beginning of your main() function
    pygame.init()

    # In your main function, instantiate a Player object
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # assignment 4:  Use pygame's display.set_mode() to get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # After initializing pygame, but before the gameloop starts, create: 
    # A new pygame.time.Clock object.
    clock = pygame.time.Clock()

    # A dt variable set to 0.
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()

    

    # assignment 5:  Create the game loop
    while True:
        # assignment 8: 
        # This will check if the user has closed the window and 
        # exit the game loop if they do. 
        # It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.shoot(shots)
                    

        # Hook the update method into the game loop by 
        # calling it on the player object each frame before rendering.
        player1.update(dt)

        # Update shots
        shots.update(dt)

        

        # After the update step in your game loop, 
        # iterate over all of the objects in your asteroids group. 
        # Check if any of them collide with the player. 
        # If a collision is detected, the program should print Game over! 
        # and immediately exit the program.
        for asteroid in asteroids:
            if asteroid.collision(player1):
                print("Game over!")
                pygame.quit()
                sys.exit()

        # iterate over all "updatables" and .update() them
        for item in updatable:
            item.update(dt)

        screen.fill(BLACK)
        
        # Draw shots
        # shots.draw(screen)
        screen.fill(BLACK)

        player1.draw(screen)
        for item in drawable:
            item.draw(screen)
        shots.draw(screen)  # Move this here

        pygame.display.flip()

        # we need to re-render the player on the screen each frame, meaning inside our game loop. 
        # Use the player.draw(screen) method
        player1.draw(screen)

        # 
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        # Divide the return value by 1000 (to convert from milliseconds to seconds) and 
        # save it into the dt variable 
        dt = (clock.tick(60)) / 1000
    
    pygame.quit()

if __name__ == "__main__":
    main()

# # sltn

# import pygame
# from constants import *

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     clock = pygame.time.Clock()
#     dt = 0

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return

#         screen.fill("black")
#         pygame.display.flip()

#         # limit the framerate to 60 FPS
#         dt = clock.tick(60) / 1000


# if __name__ == "__main__":
#     main()
