from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append([c for c in line])
        self.lines = lines

    def solve1(self):
        solution = 0
        grid = [[c for c in line] for line in self.lines]
        solution, grid = self.clear_rolls(grid)

        return solution

    def solve2(self):
        solution = 0
        grid = [[c for c in line] for line in self.lines]

        count, grid = self.clear_rolls(grid)
        while count > 0:
            solution += count
            count, grid = self.clear_rolls(grid)

        return solution

    def clear_rolls(self, grid):
        count = 0
        new_grid = [['.' for _ in line] for line in grid]

        for y, line in enumerate(grid):
            for x, c in enumerate(line):
                if c == '.':
                    continue
                adj_rolls = 0
                for dx, dy in directions2:
                    if inside_grid(x+dx, y+dy, grid) and grid[y+dy][x+dx] == '@':
                        adj_rolls += 1
                if adj_rolls < 4:
                    count += 1
                else:
                    new_grid[y][x] = '@'
        return count, new_grid


solver = Solver()
print('Solution 1: %s' % solver.solve1())
print('Solution 2: %s' % solver.solve2())