class LevelLoader:
    def __init__(self, game):
        self.game = game

    def load_level(self):
        self.game.level = self.game.levels[self.game.current_level]

    def load_levels(self, level_data):
        levels = level_data.strip().split('\n\n')
        self.game.levels = []
        for level in levels:
            rows = level.strip().split('\n')
            level_grid = []
            for row in rows:
                cells = row.strip().split()
                level_grid.append(cells)
            self.game.levels.append(level_grid)

        self.load_level()
