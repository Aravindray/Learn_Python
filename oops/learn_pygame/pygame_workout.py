# Imports
import pygame
import sys
import random

# Define Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets

# Initialize the variables

# Loop forever
while True:

    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Do any "per frame" action

    # Clear window
    window.fill(WHITE)

    # Draw the window element

    # Update the window
    pygame.display.update()

    # Slow down a bit
    clock.tick(FRAMES_PER_SECOND)
