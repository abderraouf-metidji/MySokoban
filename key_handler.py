import pygame

# Definition of arrow keys
keys = {
    'UP': pygame.K_UP,
    'DOWN': pygame.K_DOWN,
    'LEFT': pygame.K_LEFT,
    'RIGHT': pygame.K_RIGHT,
    'r': pygame.K_r,
    'n': pygame.K_n,
    'p': pygame.K_p
}

class KeyHandler:
    def __init__(self, game):
        self.game = game

    def on_key_down(self, key):

        player_x = None
        player_y = None
        
        if key in (keys['UP'], keys['DOWN'], keys['LEFT'], keys['RIGHT']):
            for test_y, row in enumerate(self.game.level):
                for test_x, cell in enumerate(row):
                    if cell == self.game.player or cell == self.game.player_on_goal_square:
                        player_x = test_x
                        player_y = test_y

            dx = 0
            dy = 0

            if key == keys['LEFT']:
                dx = -1
            elif key == keys['RIGHT']:
                dx = 1
            elif key == keys['UP']:
                dy = -1
            elif key == keys['DOWN']:
                dy = 1

            current = self.game.level[player_y][player_x]
            adjacent = self.game.level[player_y + dy][player_x + dx]

            beyond = ''
            if (
                0 <= player_y + dy + dy < len(self.game.level)
                and 0 <= player_x + dx + dx < len(self.game.level[player_y + dy + dy])
            ):
                beyond = self.game.level[player_y + dy + dy][player_x + dx + dx]

            next_adjacent = {
                self.game.empty: self.game.player,
                self.game.goal_square: self.game.player_on_goal_square
            }

            next_current = {
                self.game.player: self.game.empty,
                self.game.player_on_goal_square: self.game.goal_square,
            }

            next_beyond = {
                self.game.empty: self.game.box,
                self.game.goal_square: self.game.box_on_goal_square,
            }

            next_adjacent_push = {
                self.game.box: self.game.player,
                self.game.box_on_goal_square: self.game.player_on_goal_square,
            }

            if adjacent in next_adjacent:
                self.game.level[player_y][player_x] = next_current[current]
                self.game.level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

            elif beyond in next_beyond and adjacent in next_adjacent_push:
                self.game.level[player_y][player_x] = next_current[current]
                self.game.level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
                self.game.level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

            complete = True

            for y, row in enumerate(self.game.level):
                for x, cell in enumerate(row):
                    if cell == self.game.box:
                        complete = False

            if complete:
                self.game.current_level += 1
                if self.game.current_level >= len(self.game.levels):
                    self.game.current_level = 0
                self.game.load_level()

        elif key == keys['r']:
            self.game.load_level()

        elif key == keys['n']:
            self.game.current_level += 1
            if self.game.current_level >= len(self.game.levels):
                self.game.current_level = 0
            self.game.load_level()

        elif key == keys['p']:
            self.game.current_level -= 1
            if self.game.current_level < 0:
                self.game.current_level = len(self.game.levels) - 1
            self.game.load_level()
