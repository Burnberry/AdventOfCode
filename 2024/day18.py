from help import *


def parse_input():
    # w, h, size = 7, 7, 12
    w, h, size = 71, 71, 1024
    lines = []
    for line in get_input():
        lines.append([int(i) for i in line.split(",")])

    grid = [['.' for _ in range(w)] for _ in range(h)]

    return lines, w, h, grid, size


def solution1(lines, w, h, grid, size, part2=False):
    if not part2:
        for x, y in lines[:size]:
            grid[y][x] = '#'

    positions = [(0, 0)]
    seen = set(positions)
    goal = (w-1, h-1)
    goal_reached = False
    steps = 0

    while positions and not goal_reached:
        steps += 1
        new_positions = set()

        for x, y in positions:
            for dx, dy in directions:
                if inside_grid(x+dx, y+dy, grid) and grid[y+dy][x+dx] == '.' and (x+dx, y+dy) not in seen:
                    new_positions.add((x+dx, y+dy))
                    seen.add((x+dx, y+dy))
                    if (x+dx, y+dy) == goal:
                        goal_reached = True

        positions = new_positions

    solution = steps

    if not part2:
        print('Solution 1: %s' % solution, goal_reached)

    return goal_reached


def solution2(lines, w, h, grid, size):
    # optimisation 1: instead of +1 steps, divide split in 1/2 of all steps dot lg(steps) checks
    steps = 0
    x, y = 0, 0
    for x, y in lines:
        steps += 1
        grid[y][x] = '#'
        if not solution1(lines, w, h, grid, size, True):
            break

    solution = (x, y)

    print('Solution 2: %s,%s' % solution)


solution1(*parse_input())
solution2(*parse_input())
