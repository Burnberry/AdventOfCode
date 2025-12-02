from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            name, line = line.split(": ")
            cap, dur, fla, tex, cal = [int(l.split(" ")[-1]) for l in line.split(", ")]
            lines.append((name, cap, dur, fla, tex, cal))
        self.lines = lines

    def solve1(self):
        solution = self.get_solution([], len(self.lines), 100, self.score)

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = self.get_solution([], len(self.lines), 100, self.score2)

        print('Solution 2: %s' % solution)

    def get_solution(self, weights, items, spoons, scorer):
        if spoons == 0:
            return scorer(weights)
        if items == 1:
            return scorer(weights + [spoons])

        score = 0
        for n in range(0, spoons):
            score = max(score, self.get_solution(weights + [n], items-1, spoons-n, scorer))
        return score

    def score(self, weights):
        cap, dur, fla, tex, cal = 0, 0, 0, 0, 0
        for i, w in enumerate(weights):
            name, cap0, dur0, fla0, tex0, cal0 = self.lines[i]
            cap, dur, fla, tex, cal = cap+cap0*w, dur+dur0*w, fla+fla0*w, tex+tex0*w, cal+cal0*w
        cap, dur, fla, tex, cal = max(0, cap), max(0, dur), max(0, fla), max(0, tex), max(0, cal)
        return cap*dur*fla*tex

    def score2(self, weights):
        cap, dur, fla, tex, cal = 0, 0, 0, 0, 0
        for i, w in enumerate(weights):
            name, cap0, dur0, fla0, tex0, cal0 = self.lines[i]
            cap, dur, fla, tex, cal = cap+cap0*w, dur+dur0*w, fla+fla0*w, tex+tex0*w, cal+cal0*w
        cap, dur, fla, tex, cal = max(0, cap), max(0, dur), max(0, fla), max(0, tex), max(0, cal)
        if cal != 500:
            return 0
        return cap*dur*fla*tex


solver = Solver()
solver.solve1()
solver.solve2()
