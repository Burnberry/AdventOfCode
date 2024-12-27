from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = get_input()
        self.words = lines[0].split(':')[-1].split(',')
        self.lines = lines[2:]

    def solve(self):
        solution = 0
        for line in self.lines:
            runes = set()
            for word in self.words:
                self.add_runes(line, word, runes)
                self.add_runes(line, word[::-1], runes)
            solution += len(runes)

        print('Solution: %s' % solution)

    def add_runes(self, line, word, runes):
        i = 0
        while i < len(line):
            if line[i:i+len(word)] == word:
                for k in range(len(word)):
                    runes.add(i+k)
            i += 1


solver = Solver()
solver.solve()
