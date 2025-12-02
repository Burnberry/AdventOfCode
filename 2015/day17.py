from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.nums = []
        for num in get_input():
            self.nums.append(int(num))
        self.filleds = {}

    def solve1(self):
        solution = self.count(self.nums, 150)

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = 0
        cnt = len(self.nums)
        for key, i in self.filleds.items():
            if key < cnt:
                cnt = key
                solution = i

        print('Solution 2: %s' % solution)

    def count(self, nums, n, filled=0):
        if n == 0:
            self.filleds[filled] = 1+self.filleds.get(filled, 0)
            return 1
        elif len(nums) == 0:
            return 0

        cnt = 0
        cnt += self.count(nums[1:], n, filled)
        if nums[0] <= n:
            cnt += self.count(nums[1:], n-nums[0], filled+1)

        return cnt


solver = Solver()
solver.solve1()
solver.solve2()
