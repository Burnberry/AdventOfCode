from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.symbols = {}
        self.medicine = []
        is_medicine = False
        self.replacements = []
        self.convert = {}
        for line in get_input():
            if line == '':
                is_medicine = True
            elif not is_medicine:
                s, r = line.split(" => ")
                self.replacements.append((self.toSymbols(s)[0], self.toSymbols(r)))
                self.convert[tuple(self.toSymbols(r))] = self.toSymbols(s)[0]
            else:
                self.medicine = self.toSymbols(line)

        # extras
        self.replacement_symbols = {s for s, r in self.replacements}
        self.reaches0 = self.get_reaches(0)
        self.reaches1 = self.get_reaches(-1)

        self.symbol_to_key = {symbol: key for key, symbol in self.symbols.items()}
        self.seen = set()
        self.finished = False

        self.a, self.b = min([len(line) for line in self.convert]), max([len(line) for line in self.convert])

    def solve1(self):
        options = set()
        for symbol, replacement in self.replacements:
            for i, s in enumerate(self.medicine):
                if s == symbol:
                    options.add(tuple(self.medicine[:i] + replacement + self.medicine[i+1:]))
        solution = len(options)

        print('Solution 1: %s' % solution)

    def solve2(self):
        """properties from input data
        - Rn, Ar, C, Y are final symbols
        - * => *Rn*Ar, Rn & Ar are only output like this -> can be used to split problem in smaller problems of * inbetween
        - * => CRN*, C only present like this
        - * => Y can split the * in Rn*Ar in multiple possible substrings
        """

        Rn, Ar, C, Y = self.symbols["Rn"], self.symbols["Ar"], self.symbols["C"], self.symbols["Y"]
        replacements = []
        for s, r in self.replacements:
            if Rn in r:
                replacements.append(([s, r[0]], r[1:]))
        parts = self.split(self.medicine, Rn, Ar)

        print(len(parts[1]))
        for start, goal in replacements:
            found, steps = self.find_goal(parts[-2], goal)
            if found:
                print(start)
        #
        # print(len(parts))
        # for part in parts:
        #     print(len(part))
        # print(self.symbol_to_key[parts[0][0]])
        # print(parts[0], [self.symbols["C"]])
        # print(self.find_goal(parts[0], [self.symbols["C"]]))
        # print(self.medicine.count(Rn))

        solution = "TODO"

        print('Solution 2: %s' % solution)

    def split(self, line, up, down):
        level = 0
        part = []
        parts = [part]
        for s in line:
            if s == up:
                if level == 0:
                    part = [s]
                    parts.append(part)
                level += 1
            elif s == down:
                part.append(s)
                level -= 1
                if level == 0:
                    part = []
                    parts.append(part)
            else:
                part.append(s)
        return parts

    def toSymbols(self, line: str):
        symbols = []
        symbol = line[0]
        for c in line[1:] + 'Q':
            if c.isupper():
                if symbol not in self.symbols:
                    self.symbols[symbol] = 1+len(self.symbols)
                symbols.append(self.symbols[symbol])
                symbol = c
            else:
                symbol += c
        return symbols

    def get_reaches(self, i=0):
        reaches = {symbol: set() for key, symbol in self.symbols.items()}
        for symbol, replacement in self.replacements:
            seen = set()
            syms = [replacement[i]]
            while syms:
                for s in syms:
                    seen.add(s)
                new = set()

                for s in syms:
                    for s0, r0 in self.replacements:
                        if s == s0 and r0[i] not in seen:
                            new.add(r0[i])

                syms = new

            for s in seen:
                reaches[symbol].add(s)
        return reaches

    def step(self, i, line):
        lines = set()
        for s, r in self.replacements:
            if s == line[i]:
                new_line = line[:i] + r + line[i+1:]
                if len(new_line) > len(self.medicine):
                    continue
                if len(new_line) == len(self.medicine) and new_line == self.medicine:
                    self.finished = True
                for di in range(len(line[i:])):
                    if self.medicine[i+di] in self.reaches0[new_line[i+di]]:
                        lines.add((i+di, tuple(new_line)))

        return [(i, list(line)) for i, line in lines]

    def find_goal(self, start, goal):
        found = start == goal
        goal = tuple(goal)
        steps = 0
        lines = [start]
        while not found and lines:
            steps += 1
            new_lines = set()
            for line in lines:
                for symbol, r in self.replacements:
                    for i in range(len(line)-len(r)+1):
                        if line[i:i+len(r)] == r:
                            new_line = line[:i] + [symbol] + line[i+len(r):]
                            new_line = tuple(new_line)
                            if new_line == goal:
                                found = True
                                break
                            new_lines.add(new_line)

            lines = [list(line) for line in new_lines]
        return found, steps


solver = Solver()
solver.solve1()
solver.solve2()
