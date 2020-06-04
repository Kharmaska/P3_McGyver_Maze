"""
This module is responsible for the class Maze that will be used
to generate the labyrinth for the game
"""

import pygame
from pygame.locals import *
from constants import *

class Maze:
    """ Class handling the creation of a game maze"""
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
        Method handling the display of the maze
        based on the structure list rendered by generate()
        :param window: pygame window
        """
        # Images loading
        wall = pygame.image.load(WALL_IMG).convert()
        start = pygame.image.load(START_IMG).convert()
        end = pygame.image.load(GUARDIAN_IMG).convert_alpha()

        # Running through the level list
        num_line = 0
        for line in self.structure:
            num_square = 0
            for sprite in line:
                # Real time position calculation
                x_pos = num_square * SPRITES_SIZE
                y_pos = num_line * SPRITES_SIZE
                if sprite == 'w':
                    window.blit(wall, (x_pos, y_pos))
                elif sprite == 's':
                    window.blit(start, (x_pos, y_pos))
                elif sprite == 'e':
                    window.blit(end, (x_pos, y_pos))
                num_square += 1
            num_line += 1
