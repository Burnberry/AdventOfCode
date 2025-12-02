from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.grid = []
        for line in get_input():
            self.grid.append(list(line))

    def solve(self):
        solution = 0
        for y, row in enumerate(self.grid):
            for x, c in enumerate(row):
                if c == '#':
                    solution += self.get_depth(x, y)

        print('Solution: %s' % solution)

    def get_depth(self, x, y):
        depth = 0
        seen = {(x, y)}
        positions = {(x, y)}

        while positions:
            depth += 1
            new_positions = set()
            for x, y in positions:
                for dx, dy in directions:
                    pos = (x+dx, y+dy)
                    if inside_grid(*pos, self.grid) and pos not in seen:
                        seen.add(pos)
                        if self.grid[y+dy][x+dx] != '#':
                            return depth
                        new_positions.add(pos)

            positions = new_positions
        return depth


solver = Solver()
solver.solve()
