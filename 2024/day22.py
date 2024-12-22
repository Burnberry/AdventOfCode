from help import *


class Solver:
    def __init__(self):
        # parse inputs
        lines = []
        for line in get_input():
            lines.append(int(line))
        self.lines = lines

        # extras
        self.m = 2**24-1
        self.buyers = []

    def solve1(self):
        solution = 0
        for start in self.lines:
            secret = start
            buyer = [secret % 10]
            for _ in range(2000):
                secret = self.next_secret(secret)
                buyer.append(secret % 10)
            solution += secret
            self.buyers.append(buyer)

        print('Solution 1: %s' % solution)

    def solve2(self):
        buyer_sequences = []
        for buyer in self.buyers:
            buyer_sequences.append(self.get_buyer_sequence(buyer))

        sequences = set()
        for bs in buyer_sequences:
            for s in bs:
                sequences.add(s)

        best_sequence = False
        best_count = -1
        for sequence in sequences:
            count = 0

            for buyer_sequence in buyer_sequences:
                count += buyer_sequence.get(sequence, 0)

            if count > best_count:
                best_count = count
                best_sequence = sequence

        solution = best_count

        print('Solution 2: %s' % solution)

    def next_secret(self, secret):
        secret = (secret ^ (secret << 6)) & self.m
        secret = (secret ^ (secret >> 5)) & self.m
        secret = (secret ^ (secret << 11)) & self.m
        return secret

    def get_buyer_sequence(self, buyer):
        buyer_sequence = {}
        differences = self.get_differences(buyer)
        for i in range(3, len(differences)):
            sequence = tuple(differences[i - 3:i + 1])
            if sequence not in buyer_sequence:
                buyer_sequence[tuple(differences[i - 3:i + 1])] = buyer[i+1]
        return buyer_sequence

    def get_differences(self, buyer):
        differences = []
        for p1, p2 in zip(buyer[:-1], buyer[1:]):
            differences.append(p2-p1)
        return differences


a = Solver()
a.solve1()
a.solve2()
