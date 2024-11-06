'''Balloon Game'''

import pygame
from pygame.locals import *
import random
import pygwidgets
from balloon_constants import *
from abc import ABC, abstractmethod

class Balloon(ABC):
    '''Balloon class'''

    pop_sound_loaded = False
    pop_sound = None

    @abstractmethod
    def __init__(self, window, max_width, max_height, ID,
                 o_image, size, n_points, speed_y):
        '''Class init'''
        self.window = window
        self.ID = ID
        self.balloon_image = o_image
        self.size = size
        self.n_points = n_points
        self.speed_y = speed_y
        if not Balloon.pop_sound_loaded:
            Balloon.pop_sound_loaded = True
            Balloon.pop_sound = pygame.mixer.Sound('sounds/balloonPop.wav')

        ballon_rect = self.balloon_image.getRect()
        self.width = ballon_rect.width
        self.height = ballon_rect.height

        self.x = random.randrange(max_width - self.width)
        self.y = max_height + random.randrange(75)
        self.balloon_image.setLoc((self.x, self.y))

    def clicked_inside(self, mouse_point):
        '''Check whether balloon clicked'''
        my_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if my_rect.collidepoint(mouse_point):
            Balloon.pop_sound.play()
            return True, self.n_points
        else:
            return False, 0

    def update(self):
        '''update them image location'''
        self.y = self.y - self.speed_y
        self.balloon_image.setLoc((self.x, self.y))
        if self.y < -self.height:
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        '''draw the image in the window'''
        self.balloon_image.draw()

    def __del__(self):
        '''delete the object instance'''
        # print(self.size, 'Balloon', self.ID, 'is going away')

class BalloonSmall(Balloon):
    '''Draw the small balloon'''
    balloon_image = pygame.image.load('images/redBalloonSmall.png')

    def __init__(self, window, max_width, max_height, ID):
        '''Object initialization'''
        o_image = pygwidgets.Image(window, (0, 0), BalloonSmall.balloon_image)
        super().__init__(window, max_width, max_height, ID, o_image, 'small', 30, 3.1)

class BalloonMedium(Balloon):
    '''Draw medium size balloon'''
    balloon_image = pygame.image.load('images/redBalloonMedium.png')

    def __init__(self, window, max_width, max_height, ID):
        '''Object Initialization'''
        o_image = pygwidgets.Image(window, (0, 0), BalloonMedium.balloon_image)
        super().__init__(window, max_width, max_height, ID, o_image, 'Medium', 20, 2.2)

class BalloonLarge(Balloon):
    '''Draw large size balloon'''
    balloon_image = pygame.image.load('images/redBalloonLarge.png')
    def __init__(self, window, max_width, max_height, ID):
        '''Object Initialization'''
        o_image = pygwidgets.Image(window, (0, 0), BalloonLarge.balloon_image)
        super().__init__(window, max_width, max_height, ID, o_image, 'Large', 10, 1.5)
