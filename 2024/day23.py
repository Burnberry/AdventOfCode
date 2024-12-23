from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.connections = {}
        self.nodes, self.t_nodes = set(), set()
        for line in get_input():
            a, b = line.split('-')
            for x, y in [(a, b), (b, a)]:
                connection = self.connections.get(x, set())
                self.connections[x] = connection
                connection.add(y)
                self.nodes.add(x)
                if x[0] == 't':
                    self.t_nodes.add(x)

    def solve1(self):
        triples, nodes = self.get_triples(self.t_nodes)

        solution = len(triples)
        print('Solution 1: %s' % solution)

    def solve2(self):

        groups, nodes = self.get_triples(self.nodes)
        while len(groups) > 1:
            groups = self.get_next_groups(groups)

        group = list(groups)[0]
        solution = ("%s,"*len(group) % tuple(group))[:-1]
        print('Solution 2: %s' % solution)

    def get_triples(self, nodes):
        triples, triple_nodes = set(), set()
        for t_node in nodes:
            t_connection = self.connections[t_node]
            for node in t_connection:
                connection: set = self.connections[node]
                for node2 in connection.intersection(t_connection):
                    triple_nodes.add(t_node)
                    triple_nodes.add(node)
                    triple_nodes.add(node2)
                    triple = [t_node, node, node2]
                    triple.sort()
                    triples.add(tuple(triple))
        return triples, triple_nodes

    def get_next_groups(self, groups):
        new_groups = set()
        for group in groups:
            connection = self.connections[group[0]]
            for node in group[1:]:
                connection = connection.intersection(self.connections[node])
            for node in connection:
                new_group = [*group, node]
                new_group.sort()
                new_groups.add(tuple(new_group))
        return new_groups


solver = Solver()
solver.solve1()
solver.solve2()
