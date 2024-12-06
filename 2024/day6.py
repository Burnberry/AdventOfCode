from help import *


def parse_input():
    grid = []
    for line in get_input():
        grid.append(list(line))

    translate_dir = {
        '<': (-1, 0),
        '>': (1, 0),
        '^': (0, -1),
        'v': (0, 1),
    }

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c not in ['#', '.']:
                dx, dy = translate_dir[c]
                state = x, y, dx, dy

    return grid, state


def solution1(grid, state):
    original_state = state
    positions, states = set(), set()

    while state not in states:
        x, y, dx, dy = state
        grid[y][x] = 'X'
        positions.add((x, y))
        states.add(state)
        state = next_state(grid, state)

    solution = len(positions)
    print('Solution 1: %s' % solution)

    # part 2
    x, y, dx, dy = original_state
    positions.remove((x, y))
    loops = set()
    for x, y in positions:
        grid[y][x] = '#'

        positions, states = set(), set()
        state2 = original_state
        loop = True
        while state2 not in states:
            x2, y2, dx2, dy2 = state2
            grid[y2][x2] = 'X'
            positions.add((x2, y2))
            states.add(state2)
            state3 = next_state(grid, state2)
            if state3 == state2:
                loop = False
                break
            state2 = state3
        if loop:
            loops.add((x, y))

        grid[y][x] = '.'

    solution = len(loops)
    print('Solution 2: %s' % solution)


rotate = {
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1)
}


def next_state(grid, state):
    x, y, dx, dy = state
    if not inside_grid(x+dx, y+dy, grid):
        return state
    elif grid[y+dy][x+dx] not in ['.', 'X']:
        dx, dy = rotate[(dx, dy)]
        return x, y, dx, dy
    x += dx
    y += dy
    return x, y, dx, dy


solution1(*parse_input())
