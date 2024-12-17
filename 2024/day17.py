from help import *


def parse_input():
    registers = []
    program = []
    for i, line in enumerate(get_input()):
        if i < 3:
            registers.append(int(line.split()[-1].strip()))
        if i == 4:
            program = [int(i) for i in line.split(': ')[-1].split(',')]
    return *registers, program


def solution1(a, b, c, program, no_print=False):
    p = 0
    size = len(program)
    values = []

    while p < size:
        opcode, operand = program[p:p+2]
        combo = operand
        if operand > 3:
            if operand == 4:
                combo = a
            elif operand == 5:
                combo = b
            elif operand == 6:
                combo = c

        if opcode == 0:
            a //= 2**combo
        elif opcode == 1:
            b ^= operand
        elif opcode == 2:
            b = combo%8
        elif opcode == 3:
            if a > 0:
                p = operand
                continue
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            values.append(combo%8)
        elif opcode == 6:
            b = a // (2**combo)
        elif opcode == 7:
            c = a // (2**combo)
        p += 2

    solution = ('%s,'*len(values) % tuple(values))[:-1]

    if not no_print:
        print('Solution 1: %s' % solution)
    return solution


def solution2(a, b, c, program):
    # Property: the nth last output only depends on the last 3*n bits of a
    # - program is a simple loop, same operations are done each time
    # - a%8 is applied each loop to a
    # - b and c fully depend on the value of a in each loop, previous b, c values don't affect future loops

    # strategy:
    # given all 3(n-1) bits which produce the last n-1 outputs,
    # check all 3 bits numbers added and left pad them and check which also match the output

    goal = ('%s'*len(program) % tuple(program))

    vals = [0]
    i = 0
    while i < len(goal):
        i += 1
        new_vals = []
        for a0 in vals:
            a0 *= 2**3
            for a1 in range(2**3):
                output = solution1(a0+a1, b, c, program, True).replace(',', '')
                if output == goal[-i:]:
                    new_vals.append(a0+a1)

        vals = new_vals

    # smallest numbers are always added first -> index 0 is smallest
    a = int(vals[0])
    output = solution1(a, b, c, program, True)
    program = ('%s,'*len(program) % tuple(program))[:-1]

    if program == output:
        solution = a
    else:
        solution = 'Not equal'

    print('Solution 2: %s' % solution)


solution1(*parse_input())
solution2(*parse_input())
