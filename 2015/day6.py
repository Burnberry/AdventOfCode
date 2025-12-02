from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            a, _, b = line.split(' ')[-3:]
            x0, y0 = [int(i) for i in a.split(',')]
            x1, y1 = [int(i) for i in b.split(',')]
            if "turn off" in line:
                opp = "turn off"
            if "turn on" in line:
                opp = "turn on"
            if "toggle" in line:
                opp = "toggle"

            lines.append((opp, (x0, y0), (x1, y1)))
        self.lines = lines

    def solve1(self):
        grid = [[False for _ in range(1000)] for _ in range(1000)]
        for opp, (x0, y0), (x1, y1) in self.lines:
            for row in grid[y0:y1+1]:
                for i, v in enumerate(row[x0:x1+1]):
                    if opp == "turn off":
                        row[i+x0] = False
                    elif opp == "turn on":
                        row[i+x0] = True
                    elif opp == "toggle":
                        row[i+x0] = not v

        solution = 0
        for row in grid:
            solution += sum(row)

        print('Solution 1: %s' % solution)

    def solve2(self):
        grid = [[0 for _ in range(1000)] for _ in range(1000)]
        for opp, (x0, y0), (x1, y1) in self.lines:
            for row in grid[y0:y1+1]:
                for i, v in enumerate(row[x0:x1 + 1]):
                    if opp == "turn off":
                        row[i+x0] = max(0, v-1)
                    elif opp == "turn on":
                        row[i+x0] = v+1
                    elif opp == "toggle":
                        row[i+x0] = v+2

        solution = 0
        for row in grid:
            solution += sum(row)

        print('Solution 2: %s' % solution)


solver = Solver()
solver.solve1()
solver.solve2()
