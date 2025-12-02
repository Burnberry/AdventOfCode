from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(line)
        self.lines = lines
        self.line = []
        for c in lines[0]:
            if c == '<':
                self.line.append((-1, 0))
            if c == '>':
                self.line.append((1, 0))
            if c == 'v':
                self.line.append((0, -1))
            if c == '^':
                self.line.append((0, 1))

    def solve1(self):
        x, y = 0, 0
        positions = {(0, 0)}

        for dx, dy in self.line:
            x += dx
            y += dy
            positions.add((x, y))

        solution = len(positions)
        print('Solution 1: %s' % solution)

    def solve2(self):
        x0, y0, x1, y1 = 0, 0, 0, 0
        switch = False
        positions = {(0, 0)}

        for dx, dy in self.line:
            if switch:
                x1 += dx
                y1 += dy
                x, y = x1, y1
            else:
                x0 += dx
                y0 += dy
                x, y = x0, y0
            positions.add((x, y))
            switch = not switch

        solution = len(positions)

        print('Solution 2: %s' % solution)


solver = Solver()
solver.solve1()
solver.solve2()
