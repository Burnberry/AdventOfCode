from help import *


class Solver:
    def __init__(self):
        # parse inputs
        matrix = {}
        for line in get_input():
            line = line[:-1]
            parts = line.split(' ')
            a, b, n = parts[0], parts[-1], int(parts[3])
            if parts[2] == "lose":
                n = -n

            d = matrix.get(a, {})
            matrix[a] = d
            d[b] = n

        self.matrix = matrix

    def solve1(self):
        names = list(self.matrix.keys())
        start = names.pop()
        solution = self.optimal_happiness([start], names)

        print('Solution 1: %s' % solution)

    def solve2(self):
        names = list(self.matrix.keys())
        self.matrix["me"] = {}
        for name in names:
            self.matrix["me"][name] = 0
            self.matrix[name]["me"] = 0
        solution = self.optimal_happiness(["me"], names)

        print('Solution 2: %s' % solution)

    def optimal_happiness(self, seated, unseated):
        if not unseated:
            return self.count_happiness(seated)

        n = 0
        for i in range(len(unseated)):
            n = max(n, self.optimal_happiness(seated + [unseated[i]], unseated[:i] + unseated[i+1:]))
        return n

    def count_happiness(self, seated):
        n = self.matrix[seated[0]][seated[-1]] + self.matrix[seated[-1]][seated[0]]
        for a, b in zip(seated[:-1], seated[1:]):
            n += self.matrix[a][b] + self.matrix[b][a]
        return n


solver = Solver()
solver.solve1()
solver.solve2()
