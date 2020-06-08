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
        # Loads the item's sprite
        self.item = pygame.image.load(image_path).convert_alpha
        # Defines the position of the object on the game grid
        self.maze = maze
        self.square_x, self.square_y = self.randomposition(identifier)
        self.x_pos = self.square_x * SPRITES_SIZE
        self.y_pos = self.square_y * SPRITES_SIZE
        self.itemname = itemname
    def randomposition(self, identifier):
        """ gives a random position on the map to the item created"""
        # Initialize a validation to make sure we only generate one of each item
        onmap = False
        # Loop checking if a random spot is free
        # on the 15*15 squares map with the ' ' character
        while not onmap:
            self.square_x = random.randint(0, 14)
            self.square_y = random.randint(0, 14)
            # if the sprite is not a wall or another item
            if self.maze.structure[self.square_y][self.square_x] == ' ':
                 # then we add the item identifier to the map like 'b' for bottle
                self.maze.structure[self.square_y][self.square_x] = identifier
                # then we exit the loop by moving the validation to True and making sure
                # we do not exceed the maximum amount of 1 item
                onmap = True
        print('position de :' + identifier, self.square_x, self.square_y)
        return self.square_x, self.square_y
    def draw(self, background, image_path):
        """ Mehtod responsible to draw the game object on top of the game background"""
        self.itemname = pygame.image.load(image_path).convert_alpha()
        background.blit(self.itemname, (self.x_pos, self.y_pos))
