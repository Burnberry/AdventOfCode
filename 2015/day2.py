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
        for line in self.lines:
            l, w, h = [int(i) for i in line.split('x')]
            solution += 2*(l*w + l*h + w*h) + min([l*w, l*h, w*h])

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = 0
        for line in self.lines:
            vals = [int(i) for i in line.split('x')]
            l, w, h = vals
            vals.sort()
            solution += 2*(vals[0] + vals[1]) + l*w*h


        print('Solution 2: %s' % solution)


solver = Solver()
solver.solve1()
solver.solve2()
