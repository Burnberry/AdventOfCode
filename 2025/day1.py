from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(line)
        self.lines = lines

    def solve1(self):
        solution = 0

        position = 50
        for line in self.lines:
            c, n = line[0], int(line[1:])
            if c == 'L':
                n = -n
            position += n
            if (position % 100) == 0:
                solution += 1

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = 0

        position = 50
        for line in self.lines:
            c, n = line[0], int(line[1:])
            if c == 'L':
                dx = -1
            else:
                dx = 1
            for i in range(n):
                position += dx
                position %= 100
                if position == 0:
                    solution += 1

        print('Solution 2: %s' % solution)


solver = Solver()
solver.solve1()
solver.solve2()
