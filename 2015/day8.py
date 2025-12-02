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
            solution += len(line) - self.count_mem(line)

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = 0
        for line in self.lines:
            solution += self.count2(line)

        print('Solution 2: %s' % solution)

    def count_mem(self, line):
        n = 0
        hexa = "0123456789abcdef"
        line = line[1:-1]
        while line:
            n += 1
            if line[0] != '\\':
                line = line[1:]
            elif line[:2] == '\\x' and len(line[2:4]) == 2 and line[2] in hexa and line[3] in hexa:
                line = line[4:]
            else:
                line = line[2:]
        return n

    def count2(self, line):
        line = line[1:-1]
        line = line.replace("\\", "\\\\").replace("\"", "\\\"")
        line = "\"\\\"" + line + "\\\"\""
        return len(line) - self.count_mem(line)


solver = Solver()
solver.solve1()
solver.solve2()
