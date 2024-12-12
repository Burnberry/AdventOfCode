from help import *


def parse_input():
    lines = []
    for line in get_input():
        lines.append(list(line))
    return lines,


def solution1(grid):
    regions = set()
    seen = set()
    for y, row in enumerate(grid):
        for x, plot in enumerate(row):
            if (x, y) in seen:
                continue
            regions.add(get_region(grid, x, y, seen))

    solution = 0
    for area, perimeter, c, (x, y) in regions:
        solution += perimeter*area

    print('Solution 1: %s' % solution)


def solution2(grid):
    regions = set()
    seen = set()
    for y, row in enumerate(grid):
        for x, plot in enumerate(row):
            if (x, y) in seen:
                continue
            regions.add(get_region(grid, x, y, seen, True))

    solution = 0
    for area, perimeter, c, (x, y) in regions:
        solution += perimeter * area

    print('Solution 2: %s' % solution)


def get_region(grid, x, y, seen, part2=False):
    c = grid[y][x]
    positions = {(x, y)}
    region = set()
    perimeter = 0

    while positions:
        new_positions = set()
        for x, y in positions:
            region.add((x, y))
            seen.add((x, y))
            for dx, dy in directions:
                if (x+dx, y+dy) in region:
                    continue
                elif not inside_grid(x+dx, y+dy, grid):
                    perimeter += 1
                elif grid[y+dy][x+dx] != c:
                    perimeter += 1
                else:
                    new_positions.add((x+dx, y+dy))
        positions = new_positions
    if part2:
        perimeter = custom_perimeter(region)
    return len(region), perimeter, c, (x, y)


def custom_perimeter(region):
    x0, y0, x1, y1 = get_size(region)
    w, h = x1-x0+1, y1-y0+1

    # pad with extra non-region rows
    region_yx = [[False for _ in range(w)] for _ in range(h+2)]
    region_xy = [[False for _ in range(h)] for _ in range(w+2)]

    for x, y in region:
        region_yx[y-y0+1][x-x0] = True
        region_xy[x-x0+1][y-y0] = True

    return count_flips(region_yx) + count_flips(region_xy)


def count_flips(region):
    count = 0

    for row0, row1 in zip(region[:-1], region[1:]):
        flip_state_prev = 0
        for prev, cur in zip(row0, row1):
            flip_state = 2*prev + cur
            if prev != cur and flip_state != flip_state_prev:
                count += 1
            flip_state_prev = flip_state
    return count


def get_size(region: set):
    x0, y0, x1, y1 = 1000, 1000, 0, 0
    for x, y in region:
        x0 = min(x0, x)
        y0 = min(y0, y)
        x1 = max(x1, x)
        y1 = max(y1, y)
    return x0, y0, x1, y1


solution1(*parse_input())
solution2(*parse_input())
