import sys

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

one_steps = [None for _ in range(N + 1)]
two_steps = [None for _ in range(N + 1)]
one_steps[0] = 0
two_steps[0] = 0


def one_step(idx):
    if one_steps[idx] != None:
        return one_steps[idx]
    max_cost = -INF
    if idx - 1 >= 0:
        temp = two_step(idx - 1) + stairs[idx]
        max_cost = max(max_cost, temp)
    if idx == 2:
        temp = stairs[0] + stairs[1] + stairs[2]
        max_cost = max(max_cost, temp)
    one_steps[idx] = max_cost
    return max_cost


def two_step(idx):
    if two_steps[idx] != None:
        return two_steps[idx]
    max_cost = -INF
    if idx - 2 >= 0:
        before = max(two_step(idx - 2), one_step(idx - 2))
        temp = before + stairs[idx]
        max_cost = max(max_cost, temp)
    two_steps[idx] = max_cost
    return max_cost


print(max(one_step(N), two_step(N)))
