from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            line = line.split(" ")
            lines.append((line[0], int(line[3]), int(line[6]), int(line[-2])))
        self.lines = lines

    def solve1(self):
        solution = 0
        for name, v, tf, tr in self.lines:
            solution = max(solution, self.distance(2503, v, tf, tr))

        print('Solution 1: %s' % solution)

    def solve2(self):
        scores = {name: 0 for name, *_ in self.lines}
        for t in range(1, 2503+1):
            d = 0
            winners = []
            for name, v, tf, tr in self.lines:
                d0 = self.distance(t, v, tf, tr)
                if d0 == d:
                    winners.append(name)
                elif d0 > d:
                    d = d0
                    winners = [name]
            for winner in winners:
                scores[winner] += 1

        solution = max([score for winner, score in scores.items()])
        print('Solution 2: %s' % solution)

    def distance(self, t, v, tf, tr):
        dt = t % (tf+tr)
        n = t // (tf+tr)
        return n*(v*tf) + v*min(dt, tf)


solver = Solver()
solver.solve1()
solver.solve2()
