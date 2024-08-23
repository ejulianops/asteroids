# assignment 1: import pygame at the top of your main.py file.
import pygame
from player import Player

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

    # assignment 5:  Create the game loop
    while True:
        # assignment 8: 
        # This will check if the user has closed the window and 
        # exit the game loop if they do. 
        # It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        

        screen.fill(BLACK)

        # we need to re-render the player on the screen each frame, meaning inside our game loop. 
        # Use the player.draw(screen) method
        player1.draw(screen)

        pygame.display.flip()
        # Divide the return value by 1000 (to convert from milliseconds to seconds) and 
        # save it into the dt variable 
        dt = (clock.tick(60)) / 1000
     
    pygame.quit()



if __name__ == "__main__":
    main()




# sltn

import pygame
from constants import *


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
