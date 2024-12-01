from help import *


def parse_input():
    l1, l2 = [], []
    for line in get_input():
        a, b = line.split('   ')
        l1.append(int(a))
        l2.append(int(b))
    return l1, l2


def solution1(l1: list, l2: list):
    l1.sort()
    l2.sort()
    x = sum([abs(a - b) for a, b in zip(l1, l2)])

    print('Solution 1: %s' % x)


def solution2(l1: list, l2: list):
    x = 0
    for a in set(l1):
        x += a*l1.count(a)*l2.count(a)

    print('Solution 2: %s' % x)


solution1(*parse_input())
solution2(*parse_input())
