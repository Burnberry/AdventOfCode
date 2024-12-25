from help import *


class Solver:
    def __init__(self):
        self.height = 5
        # parse inputs
        self.locks, self.keys = [], []
        new_object = False
        for line in get_input():
            if line == '':
                new_object = False
            elif not new_object:
                if line == '#####':
                    new_object = [0, 0, 0, 0, 0]
                    self.locks.append(new_object)
                else:
                    new_object = [-1, -1, -1, -1, -1]
                    self.keys.append(new_object)
            else:
                for i, c in enumerate(line):
                    new_object[i] += c == '#'

    def solve1(self):
        solution = 0
        for lock in self.locks:
            for key in self.keys:
                fits = True
                for a, b in zip(lock, key):
                    if a + b > self.height:
                        fits = False
                        continue
                if fits:
                    solution += 1

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = 'Freebie'

        print('Solution 2: %s' % solution)


solver = Solver()
solver.solve1()
solver.solve2()
