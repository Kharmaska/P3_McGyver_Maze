"""
This module is responsible for the class that will handle
the game mechanisms
"""


# Libraries imports
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
    WHITE_COLOR
)
from classes.object import GameObject
from classes.maze import Maze
from classes.player import Player


class Game:
    """
    Class used to handle all the game logic
    """

def initialize(self):
# We initialize the pygame module


# initialization of characters font used for the in-game texts
pygame.font.init()
font = pygame.font.SysFont('arial', 20)

# Pygame game window creation as a square of 600 px in order to have 15 squares of 40 px per line
# also adding 300 more pixels in order to display inventory and game texts
gameWindow = pygame.display.set_mode((WINDOW_SIZE + 300, WINDOW_SIZE))

# Setting up the game icon
gameIcon = pygame.image.load(ICON_IMAGE)
pygame.display.set_icon(gameIcon)

# Setting the title of the game on the Pygame window
pygame.display.set_caption(WINDOW_TITLE)


# Loads the background image and
# Adds the background texture to our game window
bg = pygame.image.load(BACKGROUND_IMG).convert()
background = pygame.transform.scale(bg, (WINDOW_SIZE, WINDOW_SIZE))
gameWindow.blit(background, (0, 0))



# updates the game display with pygame refresh method
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

# 2. Needle
needle = GameObject(NEEDLE_IMG, maze, 'n', 'needle')

# 3. Tube
tube = GameObject(TUBE_IMG, maze, 't', 'tube')

# creates an instance of Player as MacGyver (mcgv)
mcgv = Player(maze)
mcgv.draw(gameWindow, MACGYVER_IMG)


pygame.display.flip()

 # Game loop
while not IS_GAME_OVER:
    # Refresh rate
    pygame.time.Clock().tick(30)

    # Renders the "rules" for the game
    rules = font.render("Aidez MacGyver à passer le gardien", True, WHITE_COLOR)
    gameWindow.blit(rules, (620, 30))

    # Renders the text of the inventory
    inventoryDisplay = font.render('Objets récupérés: ' + str(mcgv.inventory), True, WHITE_COLOR)
    gameWindow.blit(background, (620, 400))
    gameWindow.blit(inventoryDisplay, (620, 400))



    for event in pygame.event.get():
        # If the user quits, passes the IS_GAME_OVER to True
        if event.type == QUIT:
            IS_GAME_OVER = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                IS_GAME_OVER = True

            elif event.key == K_RIGHT:
                mcgv.move('right')
            elif event.key == K_LEFT:
                mcgv.move('left')
            elif event.key == K_UP:
                mcgv.move('up')
            elif event.key == K_DOWN:
                mcgv.move('down')

    # Displays MacGyver at the new coordinates
    gameWindow.blit(background, (0, 0))
    maze.display(gameWindow)
    gameWindow.blit(mcgv.image, (mcgv.x_pos, mcgv.y_pos))

    pygame.display.flip()

    if (maze.structure[mcgv.square_y][mcgv.square_x] == 'b') or (
            maze.structure[mcgv.square_y][mcgv.square_x] == 't'
                ) or (
                    maze.structure[mcgv.square_y][mcgv.square_x] == 'n'):
        mcgv.getitem()
        maze.structure[mcgv.square_y][mcgv.square_x] = ''
        gameWindow.blit(background, (mcgv.x_pos, mcgv.y_pos))

    # Condition for MacGyver to end the game if reaching the Guardian (g)
    if maze.structure[mcgv.square_y][mcgv.square_x] == 'g':
        # win condition with a time delay before the game exits
        if mcgv.inventory == 3:
            won = font.render(
                "C'EST GAGNÉ: Bravo, vous avez vaincu le gardien !", True, WHITE_COLOR
                )            
            gameWindow.blit(won, (100, 200))
            pygame.display.flip()
            pygame.time.delay(3500)
            IS_GAME_OVER = True
        # loss condition with a time delay before the game exits
        else:
            lost = font.render(
                "GAME OVER: il vous manque des objets et le gardien vous a tué !", True, WHITE_COLOR
                )
            gameWindow.blit(lost, (100, 200))
            pygame.display.flip()
            pygame.time.delay(3500)
            IS_GAME_OVER = True
