from help import *


def parse_input():
    lines = []
    for line in get_input():
        lines.append(line)
    return lines[0],


def solution1(line_original):
    free_start = False
    free_end = len(line_original)%2 == 0
    line = []
    file_end = (len(line_original)-1)//2
    file_start = 0

    while len(line_original):
        if not free_start:
            n = int(line_original[0])
            line += [file_start]*n
            line_original = line_original[1:]
            free_start = True
            file_start += 1
        elif free_end:
            line_original = line_original[:-1]
            free_end = False
            file_end -= 1
        else:
            a, b = int(line_original[0]), int(line_original[-1])
            x = min(a, b)
            line += [file_end] * x
            a, b = a-x, b-x
            line_original = str(a) + line_original[1:-1] + str(b)
            if a == 0:
                line_original = line_original[1:]
                free_start = False
            if b == 0:
                line_original = line_original[:-1]
                free_end = True

    solution = 0
    for i, n in enumerate(line):
        solution += i*n

    print('Solution 1: %s' % solution)


def solution2(line_original):
    line_original = list(line_original)
    data = []
    is_data, file = True, 0
    while line_original:
        n = int(line_original.pop(0))
        data.append((is_data, n, [file*is_data]*n))
        file += is_data
        is_data = not is_data

    line, line_end = [], []

    while data:
        if data[0][0]:
            _, _, d = data.pop(0)
            line += d
        elif not data[-1][0]:
            _, _, d = data.pop()
            line_end = d + line_end
        else:
            _, n, d = data.pop()
            moved = False
            for i, (is_data, p, d2) in enumerate(data):
                if not is_data and n <= p:
                    data[i] = (False, p-n, [0]*(p-n))
                    if p-n == 0:
                        data = data[:i] + [(True, n, d)] + data[i+1:]
                    else:
                        data = data[:i] + [(True, n, d)] + data[i:]
                    line_end = [0]*n + line_end
                    moved = True
                    break
            if not moved:
                line_end = d + line_end

    line += line_end
    # print(line)
    solution = 0
    for i, n in enumerate(line):
        solution += i * n
    print('Solution 2: %s' % solution)


solution1(*parse_input())
solution2(*parse_input())
