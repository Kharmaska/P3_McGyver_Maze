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
bg = pygame.image.load("assets/background.jpg").convert()
background = pygame.transform.scale(bg, (WINDOW_SIZE, WINDOW_SIZE))
gameWindow.blit(background, (0, 0))

pygame.display.flip()

# Used to verify that the game is not over for the game loop
IS_GAME_OVER = False

# Maze generation
maze = Maze('maze.txt')
maze.generate()
maze.display(gameWindow)

# Items generation on the board
# 1. Ether
ether = GameObject(BOTTLE_IMG, maze, 'b', 'bottle')
ether.randomposition('b')
ether.draw(gameWindow, BOTTLE_IMG)
# 2. Needle
needle = GameObject(NEEDLE_IMG, maze, 'n', 'bottle')
needle.randomposition('n')
needle.draw(gameWindow, NEEDLE_IMG)
# 3. Tube
tube = GameObject(TUBE_IMG, maze, 't', 'bottle')
tube.randomposition('t')
tube.draw(gameWindow, TUBE_IMG)

pygame.display.flip()

 # Game loop
while not IS_GAME_OVER:
    # Refresh rate limitation
    pygame.time.Clock().tick(30)
    
    
    for event in pygame.event.get():
        pass
         