from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        lines2 = []
        for line in get_input():
            lines2.append(line)
            line = [arg for arg in line.split(' ') if arg != '']
            lines.append(line)
        self.lines = [[int(n) for n in line] for line in lines[:-1]]
        self.operators = lines[-1]
        self.lines2 = lines2

    def solve1(self):
        parts = [n for n in self.lines[0]]
        for line in self.lines[1:]:
            for i, (n, op) in enumerate(zip(line, self.operators)):
                if op == '+':
                    parts[i] += n
                elif op == '*':
                    parts[i] *= n

        solution = sum(parts)
        return solution

    def solve2(self):
        solution = 0
        operators = self.operators

        end_indexes = []
        for i, c in enumerate(self.lines2[-1][1:]):
            if c != ' ':
                end_indexes.append(i-1)
        max_len = max([len(line) for line in self.lines2])
        end_indexes.append(max_len - 1)

        # out of bound index workaround
        for i, line in enumerate(self.lines2):
            if len(line) < max_len:
                self.lines2[i] += ' '*(max_len-len(line))

        ranges = [(0, end_indexes[0] + 1)]
        for a, b in zip(end_indexes[:-1], end_indexes[1:]):
            ranges.append((a+2, b+1))

        num_lists = []
        for a, b in ranges:
            nums = []
            for x in range(a, b):
                num = None
                for y in range(len(self.lines2[:-1])):
                    if self.lines2[y][x] != ' ':
                        n = int(self.lines2[y][x])
                        if num is None:
                            num = n
                        else:
                            num = 10*num + n
                nums.append(num)
            num_lists.append(nums)

        for operator, nums in zip(operators, num_lists):
            num = nums[0]
            for n in nums[1:]:
                if operator == '+':
                    num += n
                else:
                    num *= n
            solution += num
        return solution


solver = Solver()
print('Solution 1: %s' % solver.solve1())
print('Solution 2: %s' % solver.solve2())
