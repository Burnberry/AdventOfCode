from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append([int(i) for i in line])
        self.lines = lines

    def solve1(self):
        solution = 0
        for line in self.lines:
            index = 0
            v10 = 0
            for i, b in enumerate(line[:-1]):
                if b > v10:
                    index = i
                    v10 = b
            v1 = max(line[index+1:])
            solution += 10*v10 + v1


        return solution

    def solve2(self):
        solution = 0
        for line in self.lines:
            offset = 0

            for n in range(11, -1, -1):
                index = 0
                voltage = 0
                for i, b in enumerate(line[offset: -n or None]):
                    if b > voltage:
                        index = i
                        voltage = b
                        if b == 9:
                            break
                solution += voltage*10**n
                offset += index + 1

        return solution


solver = Solver()
print('Solution 1: %s' % solver.solve1())
print('Solution 2: %s' % solver.solve2())
