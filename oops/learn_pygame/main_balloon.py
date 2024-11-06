'''Balloon game main code'''

# 1 - Imports
import pygame
import sys
import pygwidgets
from pygame.locals import *
from balloon_mgr import *

# 2 - Define Constant
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets
o_score_display = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                                         '', textColor=BLACK, backgroundColor=None,
                                         width=140, fontSize=24)
o_status_display = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25),
                                          '', textColor=BLACK, backgroundColor=None,
                                          width=300, fontSize=24)
o_start_button = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10),
                                       'Start')

# 5 - Initialize the variables
o_balloon_manager = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False

# 6 - Main loop
while True:

    # 7 - Check for and Handle events
    n_points_earned = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            o_balloon_manager.handle_event(event)
            the_score = o_balloon_manager.get_score()
            o_score_display.setValue('Score: ' + str(the_score))
        elif o_start_button.handleEvent(event):
            o_balloon_manager.start()
            o_score_display.setValue('Score: 0')
            playing = True
            o_start_button.disable()

    # 8 - Do any "per frame" action
    if playing:
        o_balloon_manager.update()
        n_popped = o_balloon_manager.get_popped_count()
        n_missed = o_balloon_manager.get_missed_count()
        o_status_display.setValue(
            f'Popped: {n_popped}   Missed: {n_missed}    Out of: {N_BALLOONS}'
        )
        if (n_popped + n_missed) == N_BALLOONS:
            playing = False
            o_start_button.enable()

    # 9 - Clear the window
    window.fill(WHITE)

    # 10 - Draw all window elements
    if playing:
        o_balloon_manager.draw()
    
    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    o_score_display.draw()
    o_status_display.draw()
    o_start_button.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - slow thing down a bit
    clock.tick(FRAMES_PER_SECOND)
