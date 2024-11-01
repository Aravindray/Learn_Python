'''90's screen saver'''

# imports
import pygame
import sys
import random
from pygame.locals import *
from ball import Ball

# Define Constant
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Initialize the variables
ball_list = []
for _ in range(N_BALLS):
    o_ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ball_list.append(o_ball)

# Loop forever
while True:

    # Check for and Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any "per frame" actions
    for o_ball in ball_list:
        o_ball.update()

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw the window elements
    for o_ball in ball_list:
        o_ball.draw()

    # Update the window
    pygame.display.update()

    # slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
