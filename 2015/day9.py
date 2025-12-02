from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.locations = set()
        self.distances = {}
        for line in get_input():
            a, dist = line.split(" = ")
            dist = int(dist)
            a, b = a.split(" to ")
            self.locations.add(a)
            self.locations.add(b)
            self.distances[(a, b)] = dist
            self.distances[(b, a)] = dist
        self.locations = list(self.locations)

    def solve1(self):
        solution = min([self.get_min_dist(self.locations[i], self.locations[:i] + self.locations[i+1:]) for i in range(len(self.locations))])

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = max([self.get_max_dist(self.locations[i], self.locations[:i] + self.locations[i+1:]) for i in range(len(self.locations))])

        print('Solution 2: %s' % solution)

    def get_min_dist(self, loc, locations, count=0):
        if len(locations) == 0:
            return count

        return min([self.get_min_dist(locations[i], locations[:i] + locations[i+1:], count + self.distances[(loc, locations[i])]) for i in range(len(locations))])

    def get_max_dist(self, loc, locations, count=0):
        if len(locations) == 0:
            return count

        return max([self.get_max_dist(locations[i], locations[:i] + locations[i+1:], count + self.distances[(loc, locations[i])]) for i in range(len(locations))])


solver = Solver()
solver.solve1()
solver.solve2()
