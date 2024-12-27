from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.line = get_input()[0]

    def solve(self):
        solution = 0
        i = 0
        while i < len(self.line):
            a, b = self.line[i], self.line[i + 1]
            solution += self.get_potion_cost(a) + self.get_potion_cost(b)
            if a != 'x' and b != 'x':
                solution += 2
            i += 2

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
