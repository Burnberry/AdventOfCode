from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append([int(i) for i in line])
        self.line = lines[0]

    def solve1(self):
        line = self.line
        for _ in range(40):
            line = self.step(line)

        solution = len(line)

        print('Solution 1: %s' % solution)

    def solve2(self):
        line = self.line
        for _ in range(50):
            line = self.step(line)

        solution = len(line)

        print('Solution 2: %s' % solution)

    def step(self, line):
        new_line = []
        n = 1
        prev = line[0]
        for c in line[1:] + [-1]:
            if c != prev:
                new_line += [n, prev]
                prev = c
                n = 0
            n += 1

        return new_line


solver = Solver()
solver.solve1()
solver.solve2()
