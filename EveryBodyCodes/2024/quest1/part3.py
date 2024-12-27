from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.line = get_input()[0]

    def solve(self):
        solution = 0
        i = 0
        while i < len(self.line):
            a, b, c = self.line[i], self.line[i + 1], self.line[i + 2]
            solution += self.get_potion_cost(a) + self.get_potion_cost(b) + self.get_potion_cost(c)
            solution += (3 - (a + b + c).count('x')) * (2 - (a + b + c).count('x'))
            i += 3

        print('Solution: %s' % solution)

    def get_potion_cost(self, creature):
        if creature == 'A':
            return 0
        elif creature == 'B':
            return 1
        elif creature == 'C':
            return 3
        elif creature == 'D':
            return 5
        return 0


solver = Solver()
solver.solve()
