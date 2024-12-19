from help import *


def parse_input():
    designs, symbols = [], []
    is_designs = False
    for line in get_input():
        if line == '':
            is_designs = True
        elif is_designs:
            designs.append(line)
        else:
            symbols = set(line.split(', '))
    return designs, symbols


def solution1(designs, symbols):
    solution = 0
    for design in designs:
        if can_design(design, symbols):
            solution += 1

    print('Solution 1: %s' % solution)


def solution2(designs, symbols):
    solution = 0

    for design in designs:
        counts = [1] + [0 for _ in range(len(design))]
        solution += design_count(design, symbols, counts)

    print('Solution 2: %s' % solution)


def can_design(design, symbols):
    if len(design) == 0:
        return True

    size = min(get_size(symbols), len(design))

    for i in range(size):
        if design[:i+1] in symbols:
            if can_design(design[i+1:], symbols):
                return True
    return False


def design_count(design, symbols, counts):
    count = counts.pop(0)
    if len(design) == 0:
        return count

    size = min(get_size(symbols), len(design))

    for i in range(size):
        if design[:i+1] in symbols:
            counts[i] += count

    return design_count(design[1:], symbols, counts)


def get_size(symbols):
    return max([len(s) for s in symbols])


solution1(*parse_input())
solution2(*parse_input())
