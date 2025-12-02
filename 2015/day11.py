from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(line)
        self.line = lines[0]

    def solve1(self):
        while not self.valid():
            self.next()

        solution = self.line
        print('Solution 1: %s' % solution)

    def solve2(self):
        self.next()
        while not self.valid():
            self.next()

        solution = self.line

        print('Solution 2: %s' % solution)

    def valid(self):
        for c in "iol":
            if c in self.line:
                return False
        return self.has_doubles() and self.has_straight() and not self.has_invalid()

    def has_doubles(self):
        n = 0
        prev = '?'
        for c in self.line:
            if c == prev:
                n += 1
                prev = '?'
            else:
                prev = c
            if n >= 2:
                return True
        return False

    def has_straight(self):
        n = 0
        prev = '?'
        for c in self.line:
            if ord(c) == ord(prev) + 1:
                n += 1
            else:
                n = 0
            prev = c
            if n >= 2:
                return True
        return False

    def has_invalid(self):
        for c in "iol":
            if c in self.line:
                return True
        return False

    def next(self):
        i = len(self.line)
        repeat = True
        while repeat:
            repeat = False
            i -= 1

            c = ord(self.line[i]) + 1
            if c > ord('z'):
                c = 'a'
                repeat = True
            else:
                c = chr(c)

            self.line = self.line[:i] + c + self.line[i+1:]


solver = Solver()
solver.solve1()
solver.solve2()
