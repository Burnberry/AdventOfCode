from help import *

MAX = 2**63

def parse_input():
    grid = []
    start, end = False, False
    for y, line in enumerate(get_input()):
        row = []
        for x, c in enumerate(line):
            row.append(c != '#')
            if c == 'S':
                start = x, y
            elif c == 'E':
                end = x, y
        grid.append(line)
    return grid, start, end


def solution1(grid, start, end):
    dx, dy = 1, 0
    x, y = start
    costs = {(x, y, dx, dy): 0}
    nodes = [(x, y, dx, dy)]

    while nodes:
        new_nodes = []
        for x, y, dx0, dy0 in nodes:
            cost = costs[(x, y, dx0, dy0)]
            node = (x+dx0, y+dy0, dx0, dy0)
            if grid[y+dy0][x+dx0] != '#' and cost+1 < costs.get(node, MAX):
                costs[node] = 1 + cost
                new_nodes.append(node)
            node = (x, y, dy0, dx0)
            if cost+1000 < costs.get(node, MAX):
                costs[node] = 1000 + cost
                new_nodes.append(node)
            node = (x, y, -dy0, -dx0)
            if cost + 1000 < costs.get(node, MAX):
                costs[node] = 1000 + cost
                new_nodes.append(node)

        nodes = new_nodes

    x, y = end
    solution = min([costs.get((x, y, dx, dy), 0) for dx, dy in directions])

    print('Solution 1: %s' % solution)
    return costs, end


def solution2(costs, end):
    spots = {end}
    nodes = set()
    solution1 = min([costs.get((*end, dx, dy), 0) for dx, dy in directions])
    for dx, dy in directions:
        if costs.get((*end, dx, dy), 0) == solution1:
            nodes.add((*end, dx, dy))

    while nodes:
        new_nodes = set()
        for x, y, dx, dy in nodes:
            cost = costs[x, y, dx, dy]
            node = (x-dx, y-dy, dx, dy)
            if node in costs and costs[node] == cost-1:
                spots.add((x-dx, y-dy))
                new_nodes.add(node)
            node = (x, y, dy, dx)
            if node in costs and costs[node] == cost-1000:
                spots.add((x, y))
                new_nodes.add(node)
            node = (x, y, -dy, -dx)
            if node in costs and costs[node] == cost - 1000:
                spots.add((x, y))
                new_nodes.add(node)
        nodes = new_nodes

    solution = len(spots)

    print('Solution 2: %s' % solution)


costs, end = solution1(*parse_input())
solution2(costs, end)
