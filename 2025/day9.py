from help import *


class Solver:
    def __init__(self):
        # parse inputs
        points = []
        for point in get_input():
            points.append([int(n) for n in point.split(',')])
        self.points = points

        self.lines = [(*self.points[-1], *self.points[0])]
        for i in range(len(self.points)-1):
            self.lines.append((*self.points[i], *self.points[i+1]))

        self.input_checks()  # convex loop

    def solve1(self):
        solution = 0

        for x0, y0 in self.points[:-1]:
            for x1, y1 in self.points[1:]:
                solution = max(solution, ((abs(x1-x0)+1)*(abs(y1-y0)+1)))

        return solution

    def solve2(self):
        solution = 0

        for i, (x0, y0) in enumerate(self.points[:-1]):
            for x1, y1 in self.points[i+1:]:
                if self.valid_rectangle(x0, y0, x1, y1):
                    solution = max(solution, ((abs(x1-x0)+1)*(abs(y1-y0)+1)))

        return solution

    def valid_rectangle(self, x0, y0, x1, y1):
        return not self.rectangle_intersected(x0, y0, x1, y1)

    def input_checks(self):
        # check redundant input is present
        d = None
        for x0, y0, x1, y1 in self.lines:
            dn = (x0-x1) == 0
            if dn == d:
                print("Redundant input")
            d = dn

        # check if loop is convex
        for i in range(len(self.lines)):
            for j in range(len(self.lines)-3):
                x0, y0, x1, y1 = self.lines[i]
                x2, y2, x3, y3 = self.lines[(i+j+2) % len(self.lines)]
                x0, x1, y0, y1 = min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1)
                x2, x3, y2, y3 = min(x2, x3), max(x2, x3), min(y2, y3), max(y2, y3)

                x_match = (x2 <= x0 <= x3 or x2 <= x1 <= x3) or ((x0 < x2) != (x1 < x2))
                y_match = (y2 <= y0 <= y3 or y2 <= y1 <= y3) or ((y0 < y2) != (y1 < y2))
                if x_match and y_match:
                    print("Loop is concave", i, j)

    def rectangle_intersected(self, rx0, ry0, rx1, ry1):
        rx0, rx1, ry0, ry1 = min(rx0, rx1), max(rx0, rx1), min(ry0, ry1), max(ry0, ry1)
        for x0, y0, x1, y1 in self.lines:
            x0, x1, y0, y1 = min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1)

            x_match = (rx0 < x0 < rx1 or rx0 < x1 < rx1) or ((x0 <= rx0) != (x1 <= rx0))
            y_match = (ry0 < y0 < ry1 or ry0 < y1 < ry1) or ((y0 <= ry0) != (y1 <= ry0))
            if x_match and y_match:
                return True
        return False


solver = Solver()
solver.valid_rectangle(9,5,2,3)
print('Solution 1: %s' % solver.solve1())
print('Solution 2: %s' % solver.solve2())
