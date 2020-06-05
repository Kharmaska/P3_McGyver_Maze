"""
This module is responsible for the class that will generate
the randomly placed items on the map
"""
# Libraries imports
import random
import pygame
from constants import *

# local modules/packages imports


class GameObject:
    """
    GameObject class that will allow the generation of
    all the items to pickup
    """
    def __init__(self, image_path, maze, identifier, itemname):
        # Loads the image for the player character
        self.item = pygame.image.load(image_path).convert_alpha
        # Defines the position of the object on the game grid
        self.maze = maze
        self.square_x, self.square_y = self.randomposition(identifier)
        self.x_pos = self.square_x * SPRITES_SIZE
        self.y_pos = self.square_y * SPRITES_SIZE
        self.itemname = itemname

    def draw(self, background, image_path):
        """ draws game objects on top of the game background"""
        self.itemname = pygame.image.load(image_path).convert_alpha()
        background.blit(image_path, (self.x_pos, self.y_pos))

    def randomposition(self, identifier):
        """ gives a random position on the map to the item created"""
        count_max = 1
        count = 0
        while count < count_max:
            self.x_pos = random.randint(0, 14)
            self.y_pos = random.randint(0, 14)
            if self.maze.structure[self.square_y][self.square_x] == ' ':
                self.maze.structure[self.square_y][self.square_x] = identifier
                count += 1
                break
        return self.square_x, self.square_y
