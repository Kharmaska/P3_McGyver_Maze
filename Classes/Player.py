"""
This module is responsible for the player object
It inherits its methods and arguments from the GameObject class
"""

# Libraries imports
import pygame

# Local imports
from constants import *

class Player:
    """
    This class will be responsible for the creation
    of the player's'character
    """
    def __init__(self, maze):
        """ This method initialize the player's inventory and position on the maze"""
        # Loads the character's inventory
        # TODO: Inventory class and items pick-up are still to be programmed
        self.inventory = 0
        self.image = pygame.image.load(MACGYVER_IMG).convert_alpha()
        # Character's position on the grid and size (pixels)
        # TODO: to be improved to handle the 's' position on the maze.txt instead
        self.square_x = 1
        self.square_y = 1
        self.x_pos = 40
        self.y_pos = 40

        self.maze = maze

    def move(self, direction):
        """
        Method handling the character's directions,
        and also the colision with walls
        """
        # Move to the right
        if direction == 'right':
            if self.square_x < (NUMBER_OF_SPRITES -1):
                # Checking if the new direction is not a wall
                if self.maze.structure[self.square_y][self.square_x + 1] != 'w':
                    # Move by one square
                    self.square_x += 1
                    # Calculation of the "Real" positioning in pixels
                    self.x_pos = self.square_x * SPRITES_SIZE


        # Move to the left
        if direction == 'left':
            if self.square_x > 0:
                # Checking if the new direction is not a wall
                if self.maze.structure[self.square_y][self.square_x - 1] != 'w':
                    # Move by one square
                    self.square_x -= 1
                    # Calculation of the "Real" positioning in pixels
                    self.x_pos = self.square_x * SPRITES_SIZE


        # Move up
        if direction == 'up':
            if self.square_y > 0:
                # Checking if the new direction is not a wall
                if self.maze.structure[self.square_y-1][self.square_x] != 'w':
                    # Move by one square
                    self.square_y -= 1
                    # Calculation of the "Real" positioning in pixels
                    self.y_pos = self.square_y * SPRITES_SIZE


        # Move down
        if direction == 'down':
            if self.square_y < (NUMBER_OF_SPRITES -1):
                # Checking if the new direction is not a wall
                if self.maze.structure[self.square_y + 1][self.square_x] != 'w':
                    # Move by one square
                    self.square_y += 1
                    # Calculation of the "Real" positioning in pixels
                    self.y_pos = self.square_y * SPRITES_SIZE

    def getitem(self):
        """
        This method will be responsible for the game object colision and pick-up
        """
        self.inventory += 1
        


    def draw(self, background, image_path):
        """ Mehtod responsible to draw the character on top of the game background"""
        self.image = pygame.image.load(image_path).convert_alpha()
        background.blit(self.image, (self.x_pos, self.y_pos))
        