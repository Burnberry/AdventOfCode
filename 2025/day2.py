from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(line)
        self.lines = lines

    def solve1(self):
        solution = 0
        ranges = []
        for line in self.lines:
            for ran in line.split(','):
                ranges.append((n for n in ran.split('-')))

        for a0, b0 in ranges:
            a, b = a0, b0
            if len(a) % 2:
                a = str(10**len(str(a)))
            if len(b) % 2:
                b = str(10**(len(str(b))-1) - 1)
            if int(a) > int(b):
                continue
            # data constraint: a and b are the same order of magnitude
            if int(a[:len(a)//2]) >= int(a[len(a)//2:]):
                a = int(a[:len(a)//2])
            else:
                a = int(a[:len(a)//2]) + 1

            if int(b[:len(b)//2]) <= int(b[len(b)//2:]):
                b = int(b[:len(b)//2])
            else:
                b = int(b[:len(b)//2]) - 1

            if a > b:
                continue

            n = b-a + 1
            solution += n*int(str(a)*2) + (10**len(str(a))+1)*n*(n-1)//2

        return solution

    def solve2(self):
        solution = 0
        ranges = []
        for line in self.lines:
            for ran in line.split(','):
                ranges.append((n for n in ran.split('-')))

        seen = set()
        for a0, b0 in ranges:
            for i in range(2, len(b0)+1):
                if ((len(a0)%i) == 0 or (len(b0)%i) == 0):
                    a, b = self.get_range(a0, b0, i)
                    if a and b and a <= b:
                        for x in range(a, b+1):
                            val = int(str(x)*i)
                            if val not in seen:
                                solution += val
                                seen.add(val)

        return solution

    def get_range(self, a0, b0, n):
        a, b = a0, b0
        l = max(len(a)//n, len(b)//n)
        if len(a) % n != 0:
            a = str(10**(l*n-1))
        if len(b) % n != 0:
            b = str(10**(l*n)-1)

        if a > b:
            return 0, 0

        if int(a[:l]*n) < int(a):
            a = int(a[:l]) + 1
        else:
            a = int(a[:l])

        if int(b[:l]*n) > int(b):
            b = int(b[:l]) - 1
        else:
            b = int(b[:l])

        if a > b:
            return 0, 0
        return a, b


solver = Solver()

print('Solution 1: %s' % solver.solve1())
print('Solution 2: %s' % solver.solve2())
