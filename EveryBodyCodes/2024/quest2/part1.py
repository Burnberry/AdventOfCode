from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = get_input()
        self.words = lines[0].split(':')[-1].split(',')
        self.line = lines[2]

    def solve(self):
        solution = 0
        for word in self.words:
            solution += self.line.count(word)

        print('Solution: %s' % solution)


solver = Solver()
solver.solve()
