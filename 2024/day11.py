from help import *


def parse_input():
    line = [int(i) for i in get_input()[0].split(' ')]
    return line,


def solution1(line):
    solution = 0
    for stone in line:
        solution += count_stones(stone, 25)

    print('Solution 1: %s' % solution)


def solution2(line):
    """
    (Recursion is the obvious choice here, yet I am blind and created this abomination instead)
    Tactic: Keep track of solutions for stones of 1 digit in a counter
    - counts per blink, stone
    - allow referencing seen solutions in counter (counter won't explode, proper count can be fixed later)
    """
    blinks = 75
    result, ref = [], []
    ref_results = {i: [([i], [])] for i in range(10)}
    for stone in line:
        if stone < 10:
            ref.append(stone)
        else:
            result.append(stone)
    ref_results[-1] = [(result, ref)]

    for i in range(blinks):
        for key in ref_results:
            res, _ = ref_results[key][-1]
            new_res, ref = [], []
            for _stone in res:
                for stone in blink(_stone):
                    if stone < 10:
                        ref.append(stone)
                    else:
                        new_res.append(stone)
            ref_results[key].append((new_res, ref))

    # fill in results
    keys = [i for i in range(10)]  # single digit keys loop often, no need to check if they're used
    results = {i: [] for i in range(10)}
    for b in range(blinks+1):
        for key in keys:
            ref_res = ref_results[key]
            if len(ref_res) <= b:
                continue
            result, refs = ref_res[b]
            new_refs = [(ref, b) for ref in refs]
            if b > 0:
                new_refs += results[key][-1][-1]
            res_count = len(result)
            ref_count = sum([results[ref][b-offset][0] for ref, offset in new_refs])
            count = res_count + ref_count
            results[key].append([count, res_count, ref_count, new_refs])

    res, _ = ref_results[-1][-1]
    solution = len(res)
    for i, (_, refs) in enumerate(ref_results[-1]):
        for ref in refs:
            solution += results[ref][blinks-i][0]
    print('Solution 2: %s' % solution)


def count_stones(stone, blinks):
    stones = [stone]
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            new_stones += blink(stone)
        stones = new_stones
    return len(stones)


def blink(stone):
    if stone == 0:
        return [1]
    if (l := len((s := str(stone))))%2 == 0:
        return [int(s[:l//2]), int(s[l//2:])]
    return [stone*2024]


solution1(*parse_input())
solution2(*parse_input())
