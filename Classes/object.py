"""
This module is responsible for the class object that will
be inherited by Player, Guardian and Items classes
"""

import pygame


class GameObject:
    """
    GameObject class that will allow the generation of
    all the objets (Player, Guardian and Items to pick up)
    """
    def __init__(self, image_path, x_pos, y_pos, *args):
        # Loads the image for the player character
        object_image = pygame.image.load(image_path)
        # Scales the image to the correct desired size
        self.image = pygame.transform.scale(object_image, (args[0], args[1]))
        # Defines the position of the object on the game grid
        self.x_pos = x_pos
        self.y_pos = y_pos
        # Defines the size of the sprite by it's width and height in pixels
        self.width = args[0]
        self.height = args[1]

    def draw(self, background):
        """ draws game objects on top of the game background"""
        background.blit(self.image, (self.x_pos, self.y_pos))
