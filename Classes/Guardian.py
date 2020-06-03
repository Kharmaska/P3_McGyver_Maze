


class Level:
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
        start = pygame.image.load(start_img).convert()
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