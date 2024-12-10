from help import *


def parse_input():
    lines = []
    for line in get_input():
        lines.append([int(i) for i in line])
    return lines,


def solution1(grid):
    solution = 0
    for y, row in enumerate(grid):
        for x, h in enumerate(row):
            if h == 0:
                solution += count_trails(grid, x, y)

    print('Solution 1: %s' % solution)


def solution2(grid):
    solution = 0
    for y, row in enumerate(grid):
        for x, h in enumerate(row):
            if h == 0:
                solution += count_trails2(grid, x, y)

    print('Solution 2: %s' % solution)


def count_trails(grid, x, y):
    h = grid[y][x]
    positions = {(x, y)}
    while h < 9 and len(positions):
        h += 1
        new_positions = set()

        for x, y in positions:
            for dx, dy in directions:
                if inside_grid(x+dx, y+dy, grid) and grid[y+dy][x+dx] == h:
                    new_positions.add((x+dx, y+dy))

        positions = new_positions
    return len(positions)


def count_trails2(grid, x, y):
    h = grid[y][x]
    positions = {(x, y): 1}
    while h < 9 and len(positions):
        h += 1
        new_positions = {}

        for x, y in positions:
            n = positions[(x, y)]
            for dx, dy in directions:
                if inside_grid(x+dx, y+dy, grid) and grid[y+dy][x+dx] == h:
                    new_positions[(x+dx, y+dy)] = n + new_positions.get((x+dx, y+dy), 0)

        positions = new_positions
    return sum(n for n in positions.values())


solution1(*parse_input())
solution2(*parse_input())
