from help import *


def parse_input():
    lines = []
    for line in get_input():
        lines.append(list(line))
    return lines,


def solution1(grid):
    x = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in valid_moves():
                x += count(grid, i, j, dx, dy)

    print('Solution 1: %s' % x)


def solution2(grid):
    x = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            n = 0
            for dx, dy in valid_moves2():
                n += count2(grid, i, j, dx, dy)
            if n >= 2:
                x += 1

    print('Solution 2: %s' % x)


def count(grid, x, y, dx, dy, word="XMAS"):
    n = 0
    if grid[x][y] == word[0]:
        word = word[1:]
    else:
        return n

    if len(word):
        if inside(grid, x+dx, y+dy):
            n += count(grid, x+dx, y+dy, dx, dy, word)
    if len(word) == 0:
        n += 1
    return n


def count2(grid, x, y, dx, dy):
    n = 0
    if grid[x][y] != 'A':
        return n

    if inside(grid, x+dx, y+dy) and grid[x+dx][y+dy] == 'M':
        if inside(grid, x-dx, y-dy) and grid[x-dx][y-dy] == 'S':
            n += 1
    return n


def valid_moves():
    return [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def valid_moves2():
    return [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def inside(grid, x, y):
    return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))


solution1(*parse_input())
solution2(*parse_input())
