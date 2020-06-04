#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
In this mini Python game, based on the Pygame library,
you will have to recover the 3 items inside the maze
so MacGyver can build an awesome weapon
to defeat the guardian and escape the maze.
In case an item would be missing
before facing the guardian, you lose!
"""

# Libraries imports
import pygame
from pygame.locals import *

# Local imports
from constants import *
from classes.object import GameObject
from classes.maze import Maze


# We initialize the pygame module
pygame.init()

# Pygame game window creation as a square of 750 px in order to have 15 squares of 50px per line
gameWindow = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# Setting up the game icon
gameIcon = pygame.image.load(ICON_IMAGE)
pygame.display.set_icon(gameIcon)

# Setting the title of the game on the Pygame window
pygame.display.set_caption(WINDOW_TITLE)


# Loads the background image and
# Adds the background texture to our game window
background = pygame.image.load(BACKGROUND_IMG).convert()
gameWindow.blit(background, (0, 0))

# Used to verify that the game is not over for the game loop
IS_GAME_OVER = False

 # Game loop
while not IS_GAME_OVER:
    # Refresh rate limitation
    pygame.time.Clock().tick(30)   