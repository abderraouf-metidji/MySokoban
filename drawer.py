import pygame
from pygame.rect import Rect

class Drawer:
    def __init__(self, game):
        self.game = game

    def draw(self):
        self.game.screen.fill((0, 0, 0))
        cell_size = 50

        for y, row in enumerate(self.game.level):
            for x, cell in enumerate(row):
                if cell != self.game.empty:
                    colors = {
                        self.game.player: (167, 135, 255),
                        self.game.player_on_goal_square: (158, 119, 255),
                        self.game.box: (255, 201, 126),
                        self.game.box_on_goal_square: (150, 255, 127),
                        self.game.goal_square: (156, 229, 255),
                        self.game.wall: (255, 147, 209),
                    }

                    pygame.draw.rect(
                        self.game.screen,
                        colors[cell],
                        Rect(
                            x * cell_size,
                            y * cell_size,
                            cell_size,
                            cell_size
                        )
                    )

                    text = self.game.font.render(str(cell), True, (0, 0, 0))
                    text_rect = text.get_rect(
                        center=(x * cell_size + cell_size // 2, y * cell_size + cell_size // 2)
                    )
                    self.game.screen.blit(text, text_rect)