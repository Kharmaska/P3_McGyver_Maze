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


# Local imports
from classes.game import Game

# We initialize the pygame module

new_game = Game()
new_game.start_new_game()
new_game.endgame()
