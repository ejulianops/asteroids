# assignment 1: import pygame at the top of your main.py file.
import pygame

# assignment 3: Ensure our predefined constants imported at the top of your file
from constants import *

def main():

    # assignment 2: Initialize pygame at the beginning of your main() function
    pygame.init()

    # assignment 4:  Use pygame's display.set_mode() to get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

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
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()