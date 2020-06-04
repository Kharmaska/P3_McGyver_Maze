"""
This is the module that generates the Maze class for the game
"""

import pygame
from pygame.locals import *
from constants import *


class Maze:
    """ Class handling the creation of a game level"""
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
        """ Method handling the creation of the level
        based on the map file provided
        It creates the map based on the list provided"""
        # File opening
        with open(self.file) as file:
            level_structure = []
            # We map the file line by line
            for line in file:
                level_line = []
                # We map all the line's sprites (letters)
                for sprite in line:
                    # We ignore the end of line sprites
                    if sprite != '\n':
                        # If not end of line we add the sprite to the line
                        level_line.append(sprite)
                # We then add the line to the level list level_structure
                level_structure.append(level_line)
            # We save the level_structure
            self.structure = level_structure

    def display(self, window):
        """
        Method handling the display of the level
        based on the structure list rendered by generate()
        :param window: pygame window
        """
        # Images loading
        wall = pygame.image.load(wall_img).convert()
        start = pygame.image.load(START_IMG).convert()
        end = pygame.image.load(goal_img).convert_alpha()

        # Running through the level list
        num_line = 0
        for line in self.structure:
            num_square = 0
            for sprite in line:
                # Real time position calculation
                x = num_square * sprites_size
                y = num_line * sprites_size
                if sprite == 'w':
                    window.blit(wall, (x, y))
                elif sprite == 's':
                    window.blit(start, (x, y))
                elif sprite == 'e':
                    window.blit(end, (x, y))
                num_square += 1
            num_line += 1


class Character:
    """ Class handling the creation of the game character"""
    def __init__(self, right, left, up, down, level):
        # Character's sprites
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        # Character's position on the grid and size (pixels)
        self.square_x = 0
        self.square_y = 0
        self.x = 0
        self.y = 0
        # Default character direction
        self.direction = self.right
        # Character's level he is in
        self.level = level

    def move(self, direction):
        """Method handling character's movement"""

        # Move to the right
        if direction == 'right':
            if self.square_x < (number_of_sprites -1):
                # Checking if the new direction is not a wall
                if self.level.structure[self.square_y][self.square_x + 1] != 'w':
                    # Move by one square
                    self.square_x += 1
                    # Calculation of the "Real" positioning in pixels
                    self.x = self.square_x * sprites_size
                # Loading the correct sprite image
                self.direction = self.right

        # Move to the left
        if direction == 'left':
            if self.square_x > 0:
                # Checking if the new direction is not a wall
                if self.level.structure[self.square_y][self.square_x - 1] != 'w':
                    # Move by one square
                    self.square_x -= 1
                    # Calculation of the "Real" positioning in pixels
                    self.x = self.square_x * sprites_size
                # Loading the correct sprite image
                self.direction = self.left

        # Move up
        if direction == 'up':
            if self.square_y > 0:
                # Checking if the new direction is not a wall
                if self.level.structure[self.square_y-1][self.square_x] != 'w':
                    # Move by one square
                    self.square_y -= 1
                    # Calculation of the "Real" positioning in pixels
                    self.y = self.square_y * sprites_size
                # Loading the correct sprite image
                self.direction = self.up

        # Move down
        if direction == 'down':
            if self.square_y < (number_of_sprites -1):
                # Checking if the new direction is not a wall
                if self.level.structure[self.square_y + 1][self.square_x] != 'w':
                    # Move by one square
                    self.square_y += 1
                    # Calculation of the "Real" positioning in pixels
                    self.y = self.square_y * sprites_size
                # Loading the correct sprite image
                self.direction = self.down