'''Simple Text Class'''

import pygame
from pygame.locals import *

class SimpleText:
    '''A blue print for display text'''
    def __init__(self, window, loc, value, text_color):
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = text_color
        self.text = None
        self.set_value(value)

    def set_value(self, new_text):
        '''Render the given text'''
        if self.text == new_text:
            return

        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.text_color)

    def draw(self):
        '''draw the give text as image'''
        self.window.blit(self.text_surface, self.loc)
