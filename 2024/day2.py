from help import *


def parse_input():
    lines = []
    for line in get_input():
        lines.append([int(i) for i in line.split()])
    return lines,


def solution1(lines):
    x = 0
    for line in lines:
        if safe(line) or safe(line[::-1]):
            x += 1
    print('Solution 1: %s' % x)


def solution2(lines):
    x = 0
    for line in lines:
        if safe(line, False) or safe(line[::-1], False):
            x += 1

    print('Solution 2: %s' % x)


def safe(line, damped=True):
    i = 0
    for a, b in zip(line[:-1], line[1:]):
        if (a <= b) or (abs(a-b)) > 3:
            if damped:
                return False
            else:
                return safe(line[:i] + line[i + 1:]) or safe(line[:i + 1] + line[i + 2:])
        i += 1
    return True


solution1(*parse_input())
solution2(*parse_input())
