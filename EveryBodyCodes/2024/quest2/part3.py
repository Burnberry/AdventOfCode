from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = get_input()
        self.words = lines[0].split(':')[-1].split(',')
        self.lines = lines[2:]
        self.cols = self.get_vertical_lines(lines[2:])

    def solve(self):
        solution = 0
        runes_total = set()
        for y, line in enumerate(self.lines):
            runes = set()
            for word in self.words:
                self.add_runes(line, word, runes, True)
                self.add_runes(line, word[::-1], runes, True)
            for x in runes:
                runes_total.add((x, y))

        for x, line in enumerate(self.cols):
            runes = set()
            for word in self.words:
                self.add_runes(line, word, runes)
                self.add_runes(line, word[::-1], runes)
            for y in runes:
                runes_total.add((x, y))

        solution += len(runes_total)
        print('Solution: %s' % solution)

    def add_runes(self, line, word, runes, loop=False):
        i = 0
        l = len(line)
        if loop:
            line *= 2
        while i < len(line):
            if line[i:i+len(word)] == word:
                for k in range(len(word)):
                    runes.add((i+k)%l)
            i += 1

    def get_vertical_lines(self, lines):
        l = min(len(line) for line in lines)
        new_lines = []
        for i in range(l):
            new_line = ''
            for line in lines:
                new_line += line[i]
            new_lines.append(new_line)
        return new_lines


solver = Solver()
solver.solve()
