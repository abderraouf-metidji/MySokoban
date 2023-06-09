import pygame
import sys
from key_handler import KeyHandler
from drawer import Drawer
from level_loader import LevelLoader

class SokobanGame:
    def __init__(self):
        pygame.init()

        # Screen size
        self.screen_width = 800
        self.screen_height = 600

        # Pygame display surface
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.key_handler = KeyHandler(self)
        self.drawer = Drawer(self)
        self.level_loader = LevelLoader(self)

        # Definition of all the elements in a level
        self.player = '7'
        self.player_on_goal_square = '5'
        self.box = '3'
        self.box_on_goal_square = '4'
        self.goal_square = '2'
        self.wall = '1'
        self.empty = '0'

        self.font = pygame.font.Font(None, 36)

        self.level = []  # Define the level attribute

        self.current_level = 0  # Define the current_level attribute
        self.levels = []  # Define the levels attribute

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.key_handler.on_key_down(event.key)

            self.drawer.draw()
            pygame.display.update()
