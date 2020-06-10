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

    def start_new_game(self):
        """
        Main method for handling the creation the game
        """
        pygame.init()
        # Game window creation as a square of 600 px in order to have 15 squares of 40 px per line
        # also adding 300 more pixels in order to display inventory and game texts
        game_window = pygame.display.set_mode((WINDOW_SIZE + 300, WINDOW_SIZE))

        # Setting up the game icon
        game_icon = pygame.image.load(ICON_IMAGE)
        pygame.display.set_icon(game_icon)

        # Setting the title of the game on the Pygame window
        pygame.display.set_caption(WINDOW_TITLE)


        # Loads the background image and
        # Adds the background texture to our game window
        bg_image = pygame.image.load(BACKGROUND_IMG).convert()
        background = pygame.transform.scale(bg_image, (WINDOW_SIZE, WINDOW_SIZE))
        game_window.blit(background, (0, 0))

        # Maze generation
        maze = Maze('maze.txt')
        maze.generate()
        maze.display(game_window)

        # Items generation on the board
        # 1. Ether
        GameObject(BOTTLE_IMG, maze, 'b', 'bottle')
        # 2. Needle
        GameObject(NEEDLE_IMG, maze, 'n', 'needle')
        # 3. Tube
        GameObject(TUBE_IMG, maze, 't', 'tube')

        # creates an instance of Player as MacGyver (mcgv)
        mcgv = Player(maze)
        mcgv.draw(game_window, MACGYVER_IMG)

        # initialization of characters font used for the in-game texts
        pygame.font.init()
        font = pygame.font.SysFont('arial', 20)

        # updates the game display with pygame refresh method
        pygame.display.flip()
        # Used to verify that the game is not over for the game loop
        is_game_over = False
        # Game loop
        while not is_game_over:
            # Refresh rate
            pygame.time.Clock().tick(30)

            # Renders the "rules" for the game
            rules = font.render("Aidez MacGyver à passer le gardien", True, WHITE_COLOR)
            game_window.blit(rules, (620, 30))

            # Renders the text of the inventory
            inventory_display = font.render(
                'Objets récupérés: ' + str(mcgv.inventory), True, WHITE_COLOR
                )
            game_window.blit(background, (620, 400))
            game_window.blit(inventory_display, (620, 400))



            for event in pygame.event.get():
                # If the user quits, passes the is_game_over to True
                if event.type == QUIT:
                    is_game_over = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        is_game_over = True

                    elif event.key == K_RIGHT:
                        mcgv.move('right')
                    elif event.key == K_LEFT:
                        mcgv.move('left')
                    elif event.key == K_UP:
                        mcgv.move('up')
                    elif event.key == K_DOWN:
                        mcgv.move('down')

            # Displays MacGyver at the new coordinates
            game_window.blit(background, (0, 0))
            maze.display(game_window)
            game_window.blit(mcgv.image, (mcgv.x_pos, mcgv.y_pos))

            pygame.display.flip()

            if (maze.structure[mcgv.square_y][mcgv.square_x] == 'b') or (
                    maze.structure[mcgv.square_y][mcgv.square_x] == 't'
                        ) or (
                            maze.structure[mcgv.square_y][mcgv.square_x] == 'n'):
                mcgv.getitem()
                maze.structure[mcgv.square_y][mcgv.square_x] = ''
                game_window.blit(background, (mcgv.x_pos, mcgv.y_pos))

            # Condition for MacGyver to end the game if reaching the Guardian (g)
            if maze.structure[mcgv.square_y][mcgv.square_x] == 'g':
                # win condition with a time delay before the game exits
                if mcgv.inventory == 3:
                    won = font.render(
                        "C'EST GAGNÉ: Bravo, vous avez vaincu le gardien !", True, WHITE_COLOR
                        )
                    game_window.blit(won, (100, 200))
                    pygame.display.flip()
                    pygame.time.delay(3500)
                    is_game_over = True
                # loss condition with a time delay before the game exits
                else:
                    game_over_txt = "GAME OVER: il vous manque des objets et le gardien vous tue !"
                    lost = font.render(game_over_txt, True, WHITE_COLOR)
                    game_window.blit(lost, (100, 200))
                    pygame.display.flip()
                    pygame.time.delay(3500)
                    is_game_over = True
