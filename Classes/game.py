"""
This module is responsible for the class that will handle
the game mechanisms
"""


# Libraries imports
import sys
import pygame
from pygame.locals import (
    K_ESCAPE,
    K_RIGHT,
    K_LEFT,
    K_UP,
    K_DOWN,
    KEYDOWN,
    QUIT
    )

# Local imports
from constants import (
    WINDOW_SIZE,
    ICON_IMAGE,
    WINDOW_TITLE,
    BOTTLE_IMG,
    NEEDLE_IMG,
    TUBE_IMG,
    BACKGROUND_IMG,
    MACGYVER_IMG,
    WHITE_COLOR,
)
from classes.object import GameObject
from classes.maze import Maze
from classes.player import Player


class Game:
    """
    Class used to handle all the game logic
    """
    def __init__(self):
        """
        init method in order to give the Game class everything it needs
        to run the game loop method
        """
        pygame.init()
        pygame.font.init()
        self.game_window = pygame.display.set_mode((WINDOW_SIZE + 200, WINDOW_SIZE))
        self.maze = Maze('maze.txt')
        self.is_game_over = False
        self.end_of_maze = False
        self.bg_image = pygame.image.load(BACKGROUND_IMG).convert()
        self.background = pygame.transform.scale(self.bg_image, (WINDOW_SIZE, WINDOW_SIZE))
        self.mcgv = Player(self.maze)

    def start_new_game(self):
        """
        Main method for handling the creation the game
        """
        # creates an instance of Player as MacGyver (mcgv)
        self.mcgv.draw(self.game_window, MACGYVER_IMG)

        # Loads the self.background image and
        # Adds the self.background texture to our game window
        self.game_window.blit(self.background, (0, 0))

        # Setting up the game icon
        game_icon = pygame.image.load(ICON_IMAGE)
        pygame.display.set_icon(game_icon)

        # Setting the title of the game on the Pygame window
        pygame.display.set_caption(WINDOW_TITLE)

        # Maze generation
        self.maze.generate()
        self.maze.display(self.game_window)

        # Items generation on the board
        # 1. Ether
        GameObject(BOTTLE_IMG, self.maze, 'b', 'bottle')
        # 2. Needle
        GameObject(NEEDLE_IMG, self.maze, 'n', 'needle')
        # 3. Tube
        GameObject(TUBE_IMG, self.maze, 't', 'tube')

        font = pygame.font.SysFont('arial', 20)
        # updates the game display with pygame refresh method
        pygame.display.flip()

        # Pygame configuration to repeat the same pressed key
        pygame.key.set_repeat(200, 30)

        # Game loop
        while not self.is_game_over:
            # Renders the text of the inventory
            inventory_display = font.render(
                'Objets récupérés: ' + str(self.mcgv.inventory), True, WHITE_COLOR
                )
            self.game_window.blit(self.background, (610, 30))
            self.game_window.blit(inventory_display, (610, 30))

            for event in pygame.event.get():
                # If the user quits, passes the is_game_over to True
                if event.type == QUIT:
                    self.is_game_over = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.is_game_over = True
                    elif event.key == K_RIGHT:
                        self.mcgv.move('right')
                    elif event.key == K_LEFT:
                        self.mcgv.move('left')
                    elif event.key == K_UP:
                        self.mcgv.move('up')
                    elif event.key == K_DOWN:
                        self.mcgv.move('down')

            # Displays MacGyver at the new coordinates
            self.game_window.blit(self.background, (0, 0))
            self.maze.display(self.game_window)
            self.game_window.blit(self.mcgv.image, (self.mcgv.x_pos, self.mcgv.y_pos))
            # updates the game display with pygame refresh method
            pygame.display.flip()

            # Condition to handle the 'colision' with one of the items to pick-up
            # if MacGyver encounters one of the items identifier
            # it adds +1 to the inventory and removes the identifier on the map
            if (self.maze.structure[self.mcgv.square_y][self.mcgv.square_x] == 'b') or (
                    self.maze.structure[self.mcgv.square_y][self.mcgv.square_x] == 't') or (
                        self.maze.structure[self.mcgv.square_y][self.mcgv.square_x] == 'n'):
                self.mcgv.getitem()
                self.maze.structure[self.mcgv.square_y][self.mcgv.square_x] = ''
                self.game_window.blit(self.background, (self.mcgv.x_pos, self.mcgv.y_pos))
            # Condition to handle the 'colision' with the guardian and putting and end to the game
            if self.maze.structure[self.mcgv.square_y][self.mcgv.square_x] == 'g':
                self.end_of_maze = True
                self.is_game_over = True

    def endgame(self):
        """
        Method for handling the win or loss conditions
        when reaching the Guardian identifier on the map
        """
        font = pygame.font.SysFont('arial', 30)
        while self.end_of_maze:
            # win condition with a time delay before the game exits Python
            if self.mcgv.inventory == 3:
                won = font.render(
                    "C'EST GAGNÉ: Bravo, vous avez vaincu le gardien !", True, WHITE_COLOR
                    )
                self.game_window.blit(won, (10, 280))
                pygame.display.flip()
                pygame.time.delay(3500)
                sys.exit(0)
            # loss condition with a time delay before the game exits Python
            else:
                game_over_txt = "GAME OVER: il vous manque des objets et le gardien vous tue !"
                lost = font.render(game_over_txt, True, WHITE_COLOR)
                self.game_window.blit(lost, (10, 280))
                pygame.display.flip()
                pygame.time.delay(3500)
                sys.exit(0)
