import pygame
from classes.Post import Post
from constants import *
from helpers import screen, from_text_to_array, center_text


class TextPost(Post):
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, location, description, text, background_color, text_color):
        Post.__init__(self, location, description)
        self.bg_color = background_color
        self.text = text
        self.text_array = from_text_to_array(self.text)
        self.text_color = text_color

    def display_content(self):
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.bg_color, square)
        text_font = pygame.font.SysFont("chalkduster.ttf", TEXT_POST_FONT_SIZE)
        for row in range(len(self.text_array)):
            text = text_font.render(self.text_array[row], True, self.text_color)
            center = center_text(len(self.text_array), text, row)
            screen.blit(text, (center[0], center[1]))

