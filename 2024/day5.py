from help import *


def parse_input():
    rules = []
    updates = []
    state = 0
    for line in get_input():
        if line == '':
            state += 1
        elif state == 0:
            rules.append([int(i) for i in line.split('|')])
        else:
            updates.append([int(i) for i in line.split(',')])
    blocked_by, blocks = {}, {}
    for a, b in rules:
        blocks[a] = blocks.get(a, []) + [b]
        blocked_by[b] = blocked_by.get(b, []) + [a]

    return rules, updates, blocked_by, blocks


def solution1(rules, updates, blocked_by, blocks):
    x = 0
    for update in updates:
        if can_update(update, blocked_by, blocks):
            x += update[len(update)//2]

    print('Solution 1: %s' % x)


def solution2(rules, updates, blocked_by, blocks):
    x = 0
    for update in updates:
        if not can_update(update, blocked_by, blocks):
            x += fix_update(update, blocked_by, blocks)[len(update)//2]
    print('Solution 2: %s' % x)


def can_update(update, blocked_by, blocks):
    updated = set()
    for page in update:
        for p in blocks.get(page, []):
            if p in updated:
                return False
        updated.add(page)
    return True


def fix_update(update, blocked_by, blocks):
    while True:
        stop = False
        updated = set()
        for page in update:
            if stop:
                break
            for p in blocks.get(page, []):
                if stop:
                    break
                if p in updated:
                    update = swap(update, p, page)
                    stop = True
            updated.add(page)
        if not stop:
            return update


def swap(update, a, b):
    return update[:update.index(a)] + [b, a] + update[update.index(a)+1: update.index(b)] + update[update.index(b)+1:]


solution1(*parse_input())
solution2(*parse_input())
