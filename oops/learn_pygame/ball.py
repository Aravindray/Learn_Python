'''A ball class'''
import pygame
from pygame.locals import *
import random

class Ball:
    '''
    Load the image of ball and bounce randomly within the screen
    '''
    def __init__(self, window, window_width, window_height) -> None:
        '''Instantiate the ball object'''
        self.window = window
        self.window_WIDTH = window_width
        self.window_HEIGHT = window_height

        self.ball_image = pygame.image.load('images/ball.png')
        ball_rect = self.ball_image.get_rect()
        self.width = ball_rect.width
        self.height = ball_rect.height
        self.MAX_WIDTH = self.window_WIDTH - self.width
        self.MAX_HEIGHT = self.window_HEIGHT - self.height

        self.x = random.randrange(self.MAX_WIDTH)
        self.y = random.randrange(self.MAX_HEIGHT)

        speeds_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.x_speed = random.choice(speeds_list)
        self.y_speed = random.choice(speeds_list)

    def update(self) -> None:
        '''define the ball moving speed'''
        if (self.x < 0) or (self.x >= self.MAX_WIDTH):
            self.x_speed = -self.x_speed

        if (self.y < 0) or (self.y >= self.MAX_HEIGHT):
            self.y_speed = -self.y_speed

        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def draw(self) -> None:
        '''Draw the image on the window'''
        self.window.blit(self.ball_image, (self.x, self.y))
