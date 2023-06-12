import pygame
from drawer import Drawer
from key_handler import KeyHandler

# Level matrix
level_matrix = [
    [0, 0, 1, 1, 1],
    [0, 0, 1, 2, 1],
    [0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 3, 0, 3, 2, 1],
    [1, 2, 0, 3, 7, 1, 1, 1],
    [1, 1, 1, 1, 3, 1],
    [0, 0, 0, 1, 2, 1],
    [0, 0, 0, 1, 1, 1],
]

class SokobanGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.SysFont(None, 30)
        self.clock = pygame.time.Clock()
        self.levels = [level_matrix]  # Add level_matrix to the levels list
        self.current_level = 0
        self.level = []
        self.empty = 0
        self.wall = 1
        self.goal_square = 2
        self.box = 3
        self.player = 7
        self.player_on_goal_square = 8
        self.box_on_goal_square = 9
        self.load_level()

    def load_level(self):
        self.level = [[self.empty if cell == 0 else cell for cell in row] for row in self.levels[self.current_level]]
        self.drawer = Drawer(self)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.key_handler.on_key_down(event.key)

            self.drawer.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()