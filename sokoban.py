import pygame
from pygame import Rect
import sys, copy

#Definition of arrow keys
keys = {
    'UP' : pygame.K_UP,
    'DOWN' : pygame.K_DOWN,
    'LEFT' : pygame.K_LEFT,
    'RIGHT' : pygame.K_RIGHT,
    'r': pygame.K_r,
    'n' : pygame.K_n,
    'p' : pygame.K_p
}

pygame.init()

#Screen size
screen_width = 800
screen_height = 600

#Pygame display surface
screen = pygame.display.set_mode((screen_width, screen_height))

#Simple levels for a sokoban game
levels = [
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
]

current_level = 0

def load_level():
    global level
    level = copy.deepcopy(levels[current_level])

load_level()

#Definition of all the elements in a level
player = '@'
player_on_goal_square = '+'
box = '$'
box_on_goal_square = '*'
goal_square = '.'
wall = '#'
empty = ' '

font = pygame.font.Font(None, 36)

#What happens when a key is pressed
def on_key_down (key):

    global current_level

    if key in (keys['UP'], keys['DOWN'], keys['LEFT'], keys['RIGHT']):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_goal_square:
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

        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
            0 <= player_y + dy + dy < len(level)
            and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
        ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
            empty: player,
            goal_square: player_on_goal_square
        }

        next_current = {
            player: empty,
            player_on_goal_square: goal_square,
        }

        next_beyond = {
            empty: box,
            goal_square: box_on_goal_square,
        }

        next_adjacent_push = {
            box: player,
            box_on_goal_square: player_on_goal_square,
        }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]
        
        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

        complete = True

        for y, row in enumerate(level):
            for x, cell in enumerate(row):
                if cell == box:
                    complete = False

        if complete:
            current_level += 1
            if current_level >= len(levels):
                current_level = 0
            load_level()

    elif key == keys['r']:
        load_level()

    elif key == keys['n']:
        current_level += 1
        if current_level >= len(levels):
            current_level = 0
        load_level()

    elif key == keys['p']:
        current_level -= 1
        if current_level < 0:
            current_level = len(levels) - 1
        load_level()

#Draw of the map based on the level used
def draw():
    screen.fill((0, 0, 0))
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                cell_size = 25

                colors = {
                    player : (167, 135, 255),
                    player_on_goal_square : (158, 119, 255),
                    box : (255, 201, 126),
                    box_on_goal_square : (150, 255, 127),
                    goal_square : (156, 229, 255),
                    wall : (255, 147, 209),
                }

                pygame.draw.rect(
                    screen,
                    colors[cell],
                    Rect(
                    (x * cell_size, y * cell_size),
                    (cell_size, cell_size)
                    )
                )

                text = font.render(cell, True, (0, 0, 0))
                screen.blit(
                    text,
                    (x * cell_size, y * cell_size)
                )

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event.key)

    draw()
    pygame.display.update()