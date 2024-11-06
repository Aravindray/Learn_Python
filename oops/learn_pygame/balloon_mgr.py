'''Balloon Manager'''

import pygame
import random
import pygwidgets
from pygame.locals import *
from balloon_constants import *
from balloon import *

class BalloonMgr():
    def __init__(self, window, max_width, max_height):
        '''class initialization'''
        self.window = window
        self.max_width = max_width
        self.max_height = max_height

    def start(self):
        '''start the game'''
        self.balloon_list = []
        self.n_popped = 0
        self.n_missed = 0
        self.score = 0

        for balloon_num in range(0, N_BALLOONS):
            random_balloon_class = random.choice((BalloonSmall, BalloonLarge, BalloonMedium))
            o_ballon = random_balloon_class(self.window, self.max_width, self.max_height, balloon_num)
            self.balloon_list.append(o_ballon)

    def handle_event(self, event):
        '''handle mouse events'''
        if event.type == MOUSEBUTTONDOWN:
            for o_ballon in reversed(self.balloon_list):
                was_hit, n_points = o_ballon.clicked_inside(event.pos)
                if was_hit:
                    if n_points > 0:
                        self.balloon_list.remove(o_ballon)
                        self.n_popped = self.n_popped + 1
                        self.score = self.score + n_points
                    return

    def update(self):
        '''update the score and remove the balloon'''
        for o_ballon in self.balloon_list:
            status = o_ballon.update()
            if status == BALLOON_MISSED:
                # balloon went off the top, remove it
                self.balloon_list.remove(o_ballon)
                self.n_missed = self.n_missed + 1

    def get_score(self):
        '''return score'''
        return self.score

    def get_popped_count(self):
        '''return popped count'''
        return self.n_popped

    def get_missed_count(self):
        '''return missed count'''
        return self.n_missed

    def draw(self):
        '''draw image in window'''
        for o_balloon in self.balloon_list:
            o_balloon.draw()
