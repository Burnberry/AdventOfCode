from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        self.wires = set()
        self.start_wires = {}
        for line in get_input():
            f, y = line.split(" -> ")
            if "NOT" in f:
                opp = "NOT"
                a = f.split("NOT ")[-1]
                b = a
            elif ' ' not in f:
                a, b = f, f
                opp = False
                if a.isnumeric():
                    self.start_wires[y] = int(a)
            else:
                a, opp, b = f.split(' ')
            lines.append((a, opp, b, y))
            self.wires.add(a)
            self.wires.add(b)
            self.wires.add(y)
        self.lines = lines

        wires = set()
        for wire in self.wires:
            if not wire.isnumeric():
                wires.add(wire)
        self.wires = wires

    def solve1(self, part2=False):
        wire_vals = {key: val for key, val in self.start_wires.items()}
        seen = {wire for wire in wire_vals}
        while len(seen) < len(self.wires):
            for a, opp, b, wire in self.lines:
                if wire in seen:
                    continue
                if (not a.isnumeric() and a not in seen) or (not b.isnumeric() and b not in seen):
                    continue
                if a.isnumeric():
                    a = int(a)
                else:
                    a = wire_vals[a]
                if b.isnumeric():
                    b = int(b)
                else:
                    b = wire_vals[b]

                if not opp:
                    val = a
                elif opp == "AND":
                    val = a & b
                elif opp == "OR":
                    val = a | b
                elif opp == 'NOT':
                    val = ~a
                elif opp == 'RSHIFT':
                    val = a >> b
                elif opp == 'LSHIFT':
                    val = a << b
                else:
                    val = 0
                    print("Not a valid opp:", opp)
                seen.add(wire)
                wire_vals[wire] = val % (2**16)

        solution = wire_vals['a']
        if not part2:
            print('Solution 1: %s' % solution)
        return solution

    def solve2(self):
        self.start_wires['b'] = self.solve1(True)
        solution = self.solve1(True)

        print('Solution 2: %s' % solution)


solver = Solver()
solver.solve1()
solver.solve2()
