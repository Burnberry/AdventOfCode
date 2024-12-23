from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append((line, int(line[:-1])))
        self.lines = lines

        # extras
        self.numpad_positions = self.get_key_positions('789/456/123/ 0A')
        self.keypad_positions = self.get_key_positions(' ^A/<v>')
        self.numpad_moves = self.get_moves(self.numpad_positions)
        self.keypad_moves = self.get_moves(self.keypad_positions)
        self.cache = {}

    def solve1(self):
        solution = 0
        self.cache = {}
        depth = 3
        for line, n in self.lines:
            count = self.get_sequence_count(line, depth, self.numpad_moves)
            solution += n*count

        print('Solution 1: %s' % solution)

    def solve2(self):
        solution = 0
        self.cache = {}
        depth = 26
        for line, n in self.lines:
            count = self.get_sequence_count(line, depth, self.numpad_moves)
            solution += n * count

        print('Solution 2: %s' % solution)

    def get_sequence_count(self, line, depth, moves):
        depth -= 1
        if res := self.cache.get((line, depth)):
            return res

        total_sequence = 0

        start = 'A'
        for goal in line:
            min_count = False
            for move in moves[(start, goal)]:
                if depth == 0:
                    count = len(move)
                else:
                    count = self.get_sequence_count(move, depth, self.keypad_moves)
                if not min_count or count < min_count:
                    min_count = count
            total_sequence += min_count
            start = goal

        self.cache[(line, depth)] = total_sequence
        return total_sequence

    def get_key_positions(self, pad):
        positions = {}
        for y, row in enumerate(pad.split('/')):
            for x, c in enumerate(row):
                positions[c] = (x, y)
        return positions

    def get_moves(self, positions):
        hole = positions[' ']
        moves = {}
        for start in positions:
            for goal in positions:
                if start == ' ' or goal == ' ':
                    continue
                moves[(start, goal)] = self.get_move_sequences(positions[start], positions[goal], hole)

        return moves

    def get_move_sequences(self, start, goal, avoid, sequence=''):
        sequences = []
        if start == goal:
            return [sequence + 'A']
        elif start == avoid:
            return []

        x0, y0 = start
        x1, y1 = goal
        dx, dy = x1-x0, y1-y0

        if dx < 0:
            sequences += self.get_move_sequences((x0-1, y0), goal, avoid, sequence + '<')
        elif dx > 0:
            sequences += self.get_move_sequences((x0+1, y0), goal, avoid, sequence + '>')

        if dy < 0:
            sequences += self.get_move_sequences((x0, y0-1), goal, avoid, sequence + '^')
        elif dy > 0:
            sequences += self.get_move_sequences((x0, y0+1), goal, avoid, sequence + 'v')

        return sequences


solver = Solver()
solver.solve1()
solver.solve2()
