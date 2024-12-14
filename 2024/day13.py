from help import *
import math
import numpy as np


def parse_input():
    machines = []
    i = 0
    ax, ay, bx, by, px, py = 0, 0, 0, 0, 0, 0
    for line in get_input():
        if i < 2:
            lines = line.split(',')
            x, y = [int(i.split('+')[-1]) for i in lines]
            if i == 0:
                ax, ay = x, y
            else:
                bx, by = x, y
        if i == 2:
            lines = line.split(',')
            px, py = [int(i.split('=')[-1]) for i in lines]
            machines.append(Machine(ax, ay, bx, by, px, py))

        i += 1
        i %= 4
    return machines,


def solution1(machines):
    solution = 0
    for machine in machines:
        sols_x = machine.solve(machine.ax, machine.bx, machine.px)
        sols_y = machine.solve(machine.ay, machine.by, machine.py)
        sols = []
        # I've been tricked, deceived, bamboozled! Multiple solutions are an edge case, not the norm, cost is unlikely relevant in solution search.
        for s in sols_x:
            if s in sols_y:
                sols.append(s)
        if sols:
            solution += min(machine.cost(*sols[0]), machine.cost(*sols[-1]))

    print('Solution 1: %s' % solution)


def solution2(machines):
    e = 0.0001
    solution = 0
    for m in machines:
        m: Machine
        m.px += 10000000000000
        m.py += 10000000000000

        a = np.array([[m.ax, m.bx], [m.ay, m.by]])
        b = np.array([m.px, m.py])
        a, b = np.linalg.solve(a, b)
        if float_zero(a, e) and float_zero(b, e):
            solution += 3*int(a+e) + int(b+e)

    print('Solution 2: %s' % solution)


def float_zero(f, e):
    return 1-e < f%1 or f%1 < e


class Machine:
    def __init__(self, ax, ay, bx, by, px, py):
        self.ax, self.ay, self.bx, self.by = ax, ay, bx, by
        self.px, self.py = px, py

    def cost(self, a, b):
        return 3*a + b

    def solve(self, a, b, c):
        x = c//a
        r = c % a
        y = r//b
        r %= b

        solutions = []
        if r == 0:
            solutions.append((x, y))
        while x >= 0:
            x -= 1
            r += a
            while r - b >= 0:
                y += 1
                r -= b
            if r == 0:
                solutions.append((x, y))
        return solutions

    def get_sol1(self, a, b, p):
        gcd = math.gcd(a, b)
        lcm = math.lcm(a, b)
        c = p % lcm
        c += lcm

        x, y = self.solve(a, b, c)[-1]
        y += (lcm*((p//lcm) - 1))//b
        return x, y, lcm//a, lcm//b


solution1(*parse_input())
solution2(*parse_input())
