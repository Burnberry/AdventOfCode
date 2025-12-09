from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(tuple([int(i) for i in line.split(',')]))
        self.lines = lines
        self.distance_pairs = self.get_distance_pairs()

    def solve1(self, n=1000):
        sizes = self.get_circuit_sizes(n)

        solution = 1
        for size in sizes[:3]:
            solution *= size
        return solution

    def solve2(self):
        a, b = 0, (len(self.lines)*(len(self.lines)-1))//2 - 1
        while a != b:
            n = (a + b) // 2
            sizes = self.get_circuit_sizes(n)
            if len(sizes) == 1:
                b = n
            else:
                a = n+1

        d, (x1, _, _), (x2, _, _) = self.distance_pairs[a-1]

        solution = x1*x2
        return solution

    def get_circuit_sizes(self, n):
        distance_pairs = self.distance_pairs[:n]

        connections = {pair: [] for pair in self.lines}
        for d, p1, p2 in distance_pairs:
            connections[p1].append(p2)
            connections[p2].append(p1)

        circuits = []
        seen = set()
        for p in connections:
            if p not in seen:
                circuits.append(self.get_circuit(p, connections, seen))
        sizes = [len(circuit) for circuit in circuits]
        sizes.sort(reverse=True)

        return sizes

    def get_distance_pairs(self):
        distance_pairs = []
        for i, pair1 in enumerate(self.lines):
            for pair2 in self.lines[i+1:]:
                distance_pairs.append((self.distance(*pair1, *pair2), pair1, pair2))
        distance_pairs.sort()
        return distance_pairs

    def distance(self, x1, y1, z1, x2, y2, z2):
        return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

    def get_circuit(self, pair, connections, seen):
        circuit = {pair}
        seen.add(pair)
        todo = {pair}

        while todo:
            todo_new = set()
            for p1 in todo:
                for p2 in connections[p1]:
                    if p2 in seen:
                        continue
                    seen.add(p2)
                    todo_new.add(p2)
                    circuit.add(p2)
            todo = todo_new
        return circuit


solver = Solver()
print('Solution 1: %s' % solver.solve1())
print('Solution 2: %s' % solver.solve2())
