import pygame
from classes.Post import Post
from constants import *
from helpers import screen
from classes.Filter import *


class ImagePost(Post):
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, image_src, location, description, do_filter=None):
        Post. __init__(self, location, description)
        self.image_src = image_src
        self.filter = do_filter

    def display_content(self):
        img = pygame.image.load(self.image_src)
        img = pygame.transform.scale(img,
                                     (POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))
        if (self.filter != None):
            Filter.apply_filter(self.filter)


