from help import *


def parse_input():
    lines = []
    for line in get_input():
        lines.append(line)
    return lines,


def solution1(lines):
    x = 0
    for line in lines:
        while 'mul(' in line:
            i = line.index('mul(')
            line = line[i+4:]
            if ',' not in line or ((i:=line.index(',')) > 3):
                continue
            a = line[:i]
            if not a.isnumeric():
                continue
            line = line[i+1:]
            if ')' not in line or ((i:=line.index(')')) > 3):
                continue
            b = line[:i]
            if not b.isnumeric():
                continue
            line = line[i + 1:]
            a, b = int(a), int(b)
            x += a*b


    print('Solution 1: %s' % x)


def solution2(lines):
    x = 0
    on = True
    for line in lines:
        while 'mul(' in line:
            if not on and 'do()' in line:
                on = True
                i = line.index('do()')
                line = line[i+4:]
            elif not on:
                break

            i = line.index('mul(')
            if "don't()" in line and line.index("don't()") < i:
                on = False
                i = line.index("don't()")
                line = line[i+7:]
                continue

            line = line[i + 4:]
            if ',' not in line or ((i := line.index(',')) > 3):
                continue
            a = line[:i]
            if not a.isnumeric():
                continue
            line = line[i + 1:]
            if ')' not in line or ((i := line.index(')')) > 3):
                continue
            b = line[:i]
            if not b.isnumeric():
                continue
            line = line[i + 1:]
            a, b = int(a), int(b)
            x += a * b

    print('Solution 2: %s' % x)


solution1(*parse_input())
solution2(*parse_input())
