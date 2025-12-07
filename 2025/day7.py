from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append([c for c in line])
        self.grid = lines

    def solve1(self):
        solution = 0

        beams = {self.grid[0].index('S')}
        for line in self.grid[1:]:
            new_beams = set([b for b in beams])
            for x, c in enumerate(line):
                if c == '^' and x in beams:
                    solution += 1
                    new_beams.add(x-1)
                    new_beams.remove(x)
                    new_beams.add(x+1)
            beams = new_beams

        return solution

    def solve2(self):
        beams = {self.grid[0].index('S'): 1}
        for line in self.grid[1:]:
            new_beams = {b: count for b, count in beams.items()}
            for x, c in enumerate(line):
                if c == '^' and x in beams:
                    count = beams[x]
                    new_beams[x-1] = count + new_beams.get(x-1, 0)
                    del new_beams[x]
                    new_beams[x+1] = count + new_beams.get(x+1, 0)
            beams = new_beams

        solution = sum([count for count in beams.values()])
        return solution


solver = Solver()
print('Solution 1: %s' % solver.solve1())
print('Solution 2: %s' % solver.solve2())