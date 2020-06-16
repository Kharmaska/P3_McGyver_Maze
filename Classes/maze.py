"""
This module is responsible for the class Maze that will be used
to generate the labyrinth for the game
"""

import pygame
from constants import (
    WALL_IMG,
    START_IMG,
    GUARDIAN_IMG,
    BOTTLE_IMG,
    NEEDLE_IMG,
    TUBE_IMG,
    SPRITES_SIZE
)

class Maze:
    """ Class handling the creation of a game maze"""
    def __init__(self, file):
        self.file = file
        self.structure = []

    def generate(self):
        """ Method handling the creation of the maze
        based on the map file provided"""
        # File opening
        with open(self.file) as file:
            maze_structure = []
            # We map the file line by line
            for line in file:
                maze_line = []
                # We map all the line's sprites (letters)
                for sprite in line:
                    # We ignore the end of line sprites
                    if sprite != '\n':
                        # we keep adding the sprits to the line until we reach the end
                        maze_line.append(sprite)
                # Then the line is added to the maze_structure
                maze_structure.append(maze_line)
            # We save the maze_structure
            self.structure = maze_structure

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
        bottle = pygame.image.load(BOTTLE_IMG).convert_alpha()
        needle = pygame.image.load(NEEDLE_IMG).convert_alpha()
        tube = pygame.image.load(TUBE_IMG).convert_alpha()

        # Running through the level list
        line_num = 0
        for line in self.structure:
            square_num = 0
            for sprite in line:
                # Real time position calculation
                x_pos = square_num * SPRITES_SIZE
                y_pos = line_num * SPRITES_SIZE
                # Here we use pygame blit to display items, walls, start or end sprites
                if sprite == 'w':  # walls
                    window.blit(wall, (x_pos, y_pos))
                elif sprite == 's':  # start tile
                    window.blit(start, (x_pos, y_pos))
                elif sprite == 'g':  # end/guardian tile
                    window.blit(end, (x_pos, y_pos))
                elif sprite == 'n':  # needle tile
                    window.blit(needle, (x_pos, y_pos))
                elif sprite == 't':  # tube tile
                    window.blit(tube, (x_pos, y_pos))
                elif sprite == 'b':  # bottle tile
                    window.blit(bottle, (x_pos, y_pos))
                square_num += 1
            line_num += 1
