import pygame
from classes.ImagePost import ImagePost
from classes.Textpost import TextPost
from helpers import *
from constants import *
from test_methods import test_comment
from buttons import *
from classes.Filter import *


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    purple_filter = Filter(PURPLE, opacity_test)

    post6 = TextPost(
        "Israel",
        "Hello World",
        "How cool dnasjd nasdj asjd jasdn jsadn jas is text post",
        (216, 79, 81), (71, 144, 205))
    post_list = []
    post1 = ImagePost("Images/ronaldo.jpg", "Dubai", "Something is going on here", purple_filter)
    post2 = ImagePost("images/noa_kirel.jpg", "hello", "h11")
    post3 = ImagePost("images/ronaldo.jpg", "hello", "h11")
    post4 = ImagePost("images/noa_kirel.jpg", "hello", "h11")
    post5 = ImagePost("images/ronaldo.jpg", "hello", "h11")
    post_list.append(post1)
    post_list.append(post2)
    post_list.append(post3)
    post_list.append(post4)
    post_list.append(post5)
    post_list.append(post6)

    # TODO: add a post here

    current_index = 0
    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        current_post = post_list[current_index]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.MOUSEMOTION:
            #     mouse_pos = pygame.mouse.get_pos()
            #     if mouse_in_button(like_button, (mouse_pos[0], mouse_pos[1])):
            #         Button.hovered = True
            #     else:
            #         Button.hovered = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_in_button(like_button, (mouse_pos[0], mouse_pos[1])):
                    current_post.add_likes()
                elif mouse_in_button(comment_button, (mouse_pos[0], mouse_pos[1])):
                    comment = read_comment_from_user()
                    current_post.add_comment(comment)
                elif mouse_in_button(click_post_button, (mouse_pos[0], mouse_pos[1])):
                    current_post.reset_comments_display_index()
                    if current_index == len(post_list)-1:
                        current_index = 0
                    else:
                        current_index += 1
                elif mouse_in_button(view_more_comments_button, (mouse_pos[0], mouse_pos[1])):
                    current_post.view_more_comments()
            # Button.draw()
        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()