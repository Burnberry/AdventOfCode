def get_input():
    return [line.replace('\n', '') for line in open("input.txt", "r").readlines()]


def inside_grid(x, y, grid):
    return (0 <= x < len(grid[0])) and (0 <= y < len(grid))


def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()
