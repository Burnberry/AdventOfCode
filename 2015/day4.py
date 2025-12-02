from help import *
import hashlib


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(line)
        self.line = lines[0]

    def solve1(self):
        i = 0
        while hashlib.md5((self.line + str(i)).encode('utf-8')).hexdigest()[:5] != '00000':
            i += 1
        solution = i

        print('Solution 1: %s' % solution)

    def solve2(self):
        i = 0
        while hashlib.md5((self.line + str(i)).encode('utf-8')).hexdigest()[:6] != '000000':
            i += 1
        solution = i

        print('Solution 2: %s' % solution)


solver = Solver()
solver.solve1()
solver.solve2()
