from help import *


class Solver:
    def __init__(self):
        # parse inputs
        self.grid = []
        self.start, self.end = None, None
        for y, line in enumerate(get_input()):
            row = []
            for x, c in enumerate(line):
                row.append(c)
                if c == 'S':
                    self.start = (x, y)
                elif c == 'E':
                    self.end = (x, y)
            self.grid.append(row)

        # extras
        self.times = self.get_normal_times()
        self.dt = 100
        self.cheats = None
        self.cheat_times = None
        self.time_saved = None

    def solve1(self):
        self.get_cheats(2)
        solution = self.count_cheats()

        print('Solution 1: %s' % solution)

    def solve2(self):
        print()
        print("Solving part 2, this may take some time (+-30s)")
        self.get_cheats(20, True)
        solution = self.count_cheats()

        print('Solution 2: %s' % solution)

    def get_normal_times(self):
        steps = 0
        positions = [self.end]
        times = {self.end: 0}

        while positions:
            steps += 1
            new_positions = []
            for x, y in positions:
                for dx, dy in directions:
                    pos = (x+dx, y+dy)
                    if inside_grid(*pos, self.grid) and pos not in times and self.grid[y+dy][x+dx] != '#':
                        times[pos] = steps
                        new_positions.append(pos)
                        if pos == self.end:
                            return steps
            positions = new_positions

        return times

    def get_cheats(self, cheat_time, print_progress=False):
        self.time_saved = self.times.get(self.start)
        cheat_time = min(cheat_time, self.time_saved)

        self.cheats = set()
        self.cheat_times = set()

        positions = {self.start}
        seen = {self.start}
        self.cheat(self.start, cheat_time)

        while positions and self.time_saved >= self.dt:
            if print_progress and self.time_saved % 1000 == 0:
                print('%s/%s' % (self.time_saved, self.times.get(self.start)))
            self.time_saved -= 1
            new_positions = set()
            for x, y in positions:
                for dx, dy in directions:
                    if inside_grid(x+dx, y+dy, self.grid) and self.grid[y+dy][x+dx] != '#' and (x+dx, y+dy) not in seen:
                        new_positions.add((x+dx, y+dy))
                        seen.add((x+dx, y+dy))
                        self.cheat((x+dx, y+dy), cheat_time)
            positions = new_positions

    def cheat(self, start, cheat_time):
        positions = {start}
        seen = {start}

        for steps in range(1, cheat_time+1):
            new_positions = set()
            for x, y in positions:
                for dx, dy in directions:
                    if not inside_grid(x+dx, y+dy, self.grid) or (x+dx, y+dy) in seen:
                        continue
                    new_positions.add((x+dx, y+dy))
                    if self.grid[y+dy][x+dx] == '#':
                        continue
                    if (t := self.time_saved - self.times.get((x+dx, y+dy), 0) - steps) >= self.dt:
                        self.cheats.add((start, (x+dx, y+dy)))
                        self.cheat_times.add((start, (x+dx, y+dy), t))
            positions = new_positions

    def count_cheats(self):
        return len(self.cheats)


a = Solver()
a.solve1()
a.solve2()
