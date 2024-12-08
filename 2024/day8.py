from help import *


def parse_input():
    grid = []
    for line in get_input():
        grid.append(list(line))

    antennas = {}
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c in ['.', '#']:
                continue
            positions = antennas.get(c, [])
            positions.append((x, y))
            antennas[c] = positions
    return grid, antennas


def solution1(grid, antennas: dict):
    antinodes = set()
    for antenna, positions in antennas.items():
        for i in range(len(positions) - 1):
            for j in range(i+1, len(positions)):
                x0, y0 = positions[i]
                x1, y1 = positions[j]
                dx, dy = x0-x1, y0-y1
                if inside_grid(x0+dx, y0+dy, grid):
                    antinodes.add((x0+dx, y0+dy))
                if inside_grid(x1-dx, y1-dy, grid):
                    antinodes.add((x1-dx, y1-dy))

    solution = len(antinodes)
    print('Solution 1: %s' % solution)


def solution2(grid, antennas: dict):
    antinodes = set()
    for antenna, positions in antennas.items():
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                x0, y0 = positions[i]
                x1, y1 = positions[j]
                dx, dy = x0 - x1, y0 - y1

                while inside_grid(x0, y0, grid):
                    antinodes.add((x0, y0))
                    x0 += dx
                    y0 += dy

                while inside_grid(x1, y1, grid):
                    antinodes.add((x1, y1))
                    x1 -= dx
                    y1 -= dy

    solution = len(antinodes)
    for x, y in antinodes:
        grid[y][x] = '#'
    print_grid(grid)

    print('Solution 2: %s' % solution)


solution1(*parse_input())
solution2(*parse_input())
