from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(line)
        self.line = lines[0]

    def solve1(self):
        nums = "-0123456789"
        n = ""
        solution = 0

        for c in self.line:
            if c in nums:
                n += c
            elif n:
                solution += int(n)
                n = ""

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = self.count(self.line)

        print('Solution 2: %s' % solution)

    def count(self, line, is_object=False):
        line += ' '
        nums = "-0123456789"
        cnt = 0
        n = ""
        subline = ""
        sub_object = False
        level = 0

        for i, c in enumerate(line):
            if c in ['{', '[']:
                if level == 0:
                    sub_object = c == '{'
                level += 1
            elif c in ['}', ']']:
                level -= 1

            if subline and level == 0:
                cnt += self.count(subline[1:], sub_object)
                subline = ""

            if level:
                subline += c
            elif c in nums:
                n += c
            elif n:
                cnt += int(n)
                n = ''
            elif line[i:i+3] == "red" and is_object:
                return 0
        return cnt


solver = Solver()
solver.solve1()
solver.solve2()
