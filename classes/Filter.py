import pygame
from constants import *
from helpers import screen


class Filter:
    def __init__(self, filter_color, filter_opacity):
        self.filter_color = filter_color
        self.filter_opacity = filter_opacity

    def apply_filter(self):
        rect = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        rect.set_alpha(self.filter_opacity)
        rect.fill(self.filter_color)
        screen.blit(rect, (POST_X_POS, POST_Y_POS))
