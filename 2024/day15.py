from help import *
import copy


def parse_input():
    grid, moves = [], []
    arrow_to_dir = {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, -1),
        'v': (0, 1)
    }
    is_grid = True
    for line in get_input():
        if line == '':
            is_grid = False
        elif is_grid:
            grid.append(list(line))
        else:
            moves += [arrow_to_dir[c] for c in line]
    return grid, moves


def solution1(grid, moves):
    x, y = get_robot_position(grid)
    for dx, dy in moves:
        x, y = move(grid, x, y, dx, dy)

    solution = count_box_vals(grid)

    print('Solution 1: %s' % solution)


def solution2(grid, moves):
    double_grid(grid)

    x, y = get_robot_position(grid)
    for dx, dy in moves:
        c = grid[y+dy][x+dx]
        if c == '.':            # no box/wall
            x, y = move_robot(grid, x, y, dx, dy)
            continue
        elif c == '#':          # wall
            continue
        else:                   # push box
            if c == '[':
                box = (x+dx, y+dy)
            else:
                box = (x+dx-1, y+dy)

            # move_box() moves boxes when partially blocked -> workaround
            new_grid = copy.deepcopy(grid)
            if move_box(new_grid, *box, dx, dy):
                grid = new_grid
                x, y = move_robot(grid, x, y, dx, dy)

    solution = count_box_vals(grid, '[')

    print('Solution 2: %s' % solution)


def move(grid, x0, y0, dx, dy):
    can_move = False
    x, y = x0+dx, y0+dy
    while (c := grid[y][x]) != '#':
        if c == '.':
            can_move = True
            break
        x += dx
        y += dy

    if not can_move:
        return x0, y0

    if grid[y0+dy][x0+dx] == 'O':
        grid[y][x] = 'O'
    grid[y0+dy][x0+dx] = '@'
    grid[y0][x0] = '.'

    return x0+dx, y0+dy


def get_robot_position(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '@':
                return x, y


def count_box_vals(grid, box='O'):
    n = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == box:
                n += 100*y + x
    return n


def double_grid(grid):
    for i, line in enumerate(grid):
        new_line = []
        for c in line:
            if c in ['.', '#']:
                new_line += [c]*2
            elif c == 'O':
                new_line += ['[', ']']
            elif c == '@':
                new_line += ['@', '.']
            else:
                print("made a mistake?")
        grid[i] = new_line


def move_box(grid, x, y, dx, dy):
    # Check box movement and apply movement dfs for vertical movement
    # leaf nodes create space for parent nodes -> no overwriting
    # leaf nodes will move when parent is blocked -> create grid backup and use that when False returned

    assert grid[y][x] == '['    # assume box position start at the left

    can_move = False
    cx, cy = x+dx, y+dy
    c = grid[cy][cx]        # left side
    c2 = grid[cy][cx+1]     # right side

    if c == '#':
        return False
    if dx:
        while c != '.':
            cx += dx
            c = grid[cy][cx]
            if c == '#':
                return False
        _move_box_row_x(grid, x, y, dx)
        return True
    else:   # dy
        if c == '.' and c2 == '.':      # no box/wall, free to move
            _move_box_y(grid, x, y, dy)
            return True
        elif c == '#' or c2 == '#':     # wall
            return False
        else:                           # more boxes to check and move
            can_move = True
            # 3 ways a box can be stacked
            # - 1 single box: [ left
            # - left box: ] left
            # - right box: [ right
            if c == '[':
                can_move &= move_box(grid, cx, cy, dx, dy)
            if c == ']':
                can_move &= move_box(grid, cx-1, cy, dx, dy)
            if c2 == '[':
                can_move &= move_box(grid, cx+1, cy, dx, dy)
            if can_move:
                _move_box_y(grid, x, y, dy)
    return can_move


def _move_box_row_x(grid, x, y, dx):
    # moves full row

    prev_c = '.'
    if dx == -1:
        x -= dx
    c = grid[y][x]

    while c != '.':
        c = grid[y][x]
        grid[y][x] = prev_c
        x += dx
        prev_c = c


def _move_box_y(grid, x, y, dy):
    # moves single box

    grid[y][x] = '.'
    grid[y][x+1] = '.'
    grid[y+dy][x] = '['
    grid[y+dy][x+1] = ']'
    pass


def move_robot(grid, x, y, dx, dy):
    grid[y + dy][x + dx] = '@'
    grid[y][x] = '.'
    return x + dx, y + dy


solution1(*parse_input())
solution2(*parse_input())
