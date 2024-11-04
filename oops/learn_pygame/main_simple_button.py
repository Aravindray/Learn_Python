# Imports
import pygame
import sys
from simple_button import SimpleButton

# Define Constant
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BLACK = (0, 0, 0)
FRAMES_PER_SECOND = 30

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets

# Initialize variable
o_button = SimpleButton(window, (150, 30), 'images/buttonUp.png', 'images/buttonDown.png')

# Loop forever
while True:

    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_button.handle_event(event):
            print('User has clicked the button')

    # Do any "per frame" action

    # clear the window
    window.fill(BLACK)

    # Draw all window elements
    o_button.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
