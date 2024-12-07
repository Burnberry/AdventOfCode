from help import *


def parse_input():
    lines = []
    for line in get_input():
        res, ops = line.split(': ')
        ops = [int(i) for i in ops.split(' ')]
        lines.append((int(res), ops))
    return lines,


def solution1(operations):
    solution = 0
    for result, operation in operations:
        left_val = operation[0]
        right_vals = operation[1:]
        if (res := match(result, left_val, right_vals)) is not None:
            solution += res

    print('Solution 1: %s' % solution)


def solution2(operations):
    solution = 0
    for result, operation in operations:
        left_val = operation[0]
        right_vals = operation[1:]
        if (res := match(result, left_val, right_vals, True)) is not None:
            solution += res

    print('Solution 2: %s' % solution)


def match(result, left_val, right_vals, concat=False):
    if len(right_vals) <= 0:
        if result == left_val:
            return left_val
        else:
            return
    term = right_vals[0]
    right_vals = right_vals[1:]
    if (res := match(result, left_val+term, right_vals, concat)) is not None:
        return res
    elif (res := match(result, left_val*term, right_vals, concat)) is not None:
        return res
    elif concat and ((res := match(result, int(str(left_val)+str(term)), right_vals, concat)) is not None):
        return res


solution1(*parse_input())
solution2(*parse_input())
