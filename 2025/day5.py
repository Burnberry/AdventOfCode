from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(line)
        self.lines = lines

        self.ranges = []
        self.ingredients = []
        is_ingredient = False
        for line in self.lines:
            if line == '':
                is_ingredient = True
                continue
            if is_ingredient:
                self.ingredients.append(int(line))
            else:
                a, b = [int(i) for i in line.split('-')]
                self.ranges.append((a, b))
        self.ingredients.sort()

    def solve1(self):
        fresh_ingredients = set()

        for a, b in self.ranges:
            for i, ingredient in enumerate(self.ingredients):
                if a <= ingredient <= b:
                    fresh_ingredients.add(ingredient)
                if ingredient > b:
                    break

        solution = len(fresh_ingredients)
        return solution

    def solve2(self):
        solution = 0
        start_ids = list(set([a for a, b in self.ranges]))
        start_ids.sort()

        ranges = {}
        for a, b in self.ranges:
            ranges[a] = max(b, ranges.get(a, b))

        for i, a in enumerate(start_ids):
            if a not in ranges:
                continue
            b = ranges[a]

            to_delete = []
            for a2 in start_ids[i+1:]:
                b2 = ranges.get(a2, 0)
                if a2 <= b:
                    to_delete.append(a2)
                    b = max(b, b2)
                    ranges[a] = b
            for a2 in to_delete:
                if a2 in ranges:
                    del ranges[a2]

        for a, b in ranges.items():
            solution += (b-a) + 1

        return solution


solver = Solver()
print('Solution 1: %s' % solver.solve1())
print('Solution 2: %s' % solver.solve2())