from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(list(line))
        self.grid = lines

    def solve1(self):
        grid = self.grid
        for _ in range(100):
            grid = self.step(grid)

        solution = 0
        for row in grid:
            for c in row:
                if c == '#':
                    solution += 1

        print('Solution 1: %s' % solution)

    def solve2(self):
        grid = self.grid
        for _ in range(100):
            grid = self.step(grid)
            grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1] = ['#', '#', '#', '#']

        solution = 0
        for row in grid:
            for c in row:
                if c == '#':
                    solution += 1

        print('Solution 2: %s' % solution)

    def step(self, grid):
        new_grid = []
        for y, row in enumerate(grid):
            new_row = []
            for x, c in enumerate(row):
                power = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    if inside_grid(x+dx, y+dy, grid):
                        if grid[y+dy][x+dx] == '#':
                            power += 1
                if power == 3 or (power == 2 and c == '#'):
                    new_row.append('#')
                else:
                    new_row.append('.')
            new_grid.append(new_row)

        return new_grid


solver = Solver()
solver.solve1()
solver.solve2()
