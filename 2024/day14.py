from help import *


def parse_input():
    lines = []
    for line in get_input():
        p, v = [l.split('=')[-1] for l in line.split(' ')]
        x, y = [int(i) for i in p.split(',')]
        dx, dy = [int(i) for i in v.split(',')]
        lines.append((x, y, dx, dy))
    return lines,


def solution1(lines):
    w, h = 101, 103
    n = 100
    quadrants = [0]*4

    for x, y, dx, dy in lines:
        x, y = jump(n, x, y, dx, dy, w, h)
        if x < w//2:
            if y < h//2:
                quadrants[0] += 1
            elif y > h//2:
                quadrants[1] += 1
        elif x > w//2:
            if y < h//2:
                quadrants[2] += 1
            elif y > h//2:
                quadrants[3] += 1

    solution = 1
    for q in quadrants:
        solution *= q

    print('Solution 1: %s' % solution)


def solution2(lines):
    solution = 'TODO'
    w, h = 101, 103
    n = 10000

    positions = [(x, y) for x, y, dx, dy in lines]
    speeds = [(dx, dy) for x, y, dx, dy in lines]
    # print_grid(get_grid(positions, w, h))

    for second in range(1, n):
        new_positions = []
        for (x, y), (dx, dy) in zip(positions, speeds):
            x = (x+dx) % w
            y = (y+dy) % h
            new_positions.append((x, y))
        positions = new_positions
        if check_is_tree(positions):
            solution = second
            print_grid(get_grid(positions, w, h))
            break

    print('Solution 2: %s' % solution)


def jump(n, x, y, dx, dy, w, h):
    x += n*dx
    y += n*dy
    x %= w
    y %= h
    return x, y


def get_grid(positions, w, h):
    grid = [['.' for _ in range(w)] for _ in range(h)]
    for x, y in positions:
        grid[y][x] = '*'
    return grid


def count_sym(positions, w, h):
    positions = set(positions)
    n = 0
    for x, y in positions:
        if (w-x-1, h-y-1) in positions:
            n += 1
    return n


def check_is_tree(positions):
    positions = set(positions)
    for x, y in positions:
        dx = 1
        while (x+dx, y) in positions:
            dx += 1
            if dx == 10:
                return True
    return False


solution1(*parse_input())
solution2(*parse_input())
