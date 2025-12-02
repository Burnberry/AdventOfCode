from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(line)
        self.lines = lines
        self.vowels = set([c for c in 'aeiou'])
        self.bans = ['ab', 'cd', 'pq', 'xy']

    def solve1(self):
        solution = 0
        for line in self.lines:
            if self.req1(line) and self.req2(line) and self.req3(line):
                solution += 1

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = 0
        for line in self.lines:
            if self.req4(line) and self.req5(line):
                solution += 1

        print('Solution 2: %s' % solution)

    def req1(self, line):
        n = 0
        for v in self.vowels:
            n += line.count(v)
        return n >= 3

    def req2(self, line):
        for a, b in zip(line[:-1], line[1:]):
            if a == b:
                return True
        return False

    def req3(self, line):
        for ban in self.bans:
            if ban in line:
                return False
        return True

    def req4(self, line):
        i = 2
        for a, b in zip(line[:-1], line[1:]):
            if (a + b) in line[i:]:
                return True
            i += 1
        return False

    def req5(self, line):
        for a, b in zip(line[:-2], line[2:]):
            if a == b:
                return True
        return False



solver = Solver()
solver.solve1()
solver.solve2()
