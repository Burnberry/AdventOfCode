from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.aunts = []
        for line in get_input():
            i = line.index(':')
            a, b = line[:i], line[i+2:]
            n = int(a.split(' ')[-1])
            vals = {}
            for val in b.split(", "):
                key, i = val.split(": ")
                vals[key] = int(i)
            self.aunts.append((n, vals))

        self.vals = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }

    def solve1(self):
        solution = "Not Found"
        for n, vals in self.aunts:
            is_sue = True
            for key, i in vals.items():
                if self.vals[key] != i:
                    is_sue = False
                    break
            if is_sue:
                solution = n

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = "Not Found"
        for n, vals in self.aunts:
            is_sue = True
            for key, i in vals.items():
                if key in ["cats", "trees"]:
                    if self.vals[key] >= i:
                        is_sue = False
                        break
                elif key in ["pomeranians", "goldfish"]:
                    if self.vals[key] <= i:
                        is_sue = False
                        break
                elif self.vals[key] != i:
                    is_sue = False
                    break
            if is_sue:
                solution = n

        print('Solution 2: %s' % solution)


solver = Solver()
solver.solve1()
solver.solve2()
