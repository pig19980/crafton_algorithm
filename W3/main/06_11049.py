# 10:00 11:16
import sys, math

input = sys.stdin.readline


N = int(input())

shape = [[None for _ in range(N)] for _ in range(N + 1)]
costs = [[math.inf for _ in range(N)] for _ in range(N + 1)]

for idx in range(N):
    costs[1][idx] = 0

for idx in range(N):
    m, k = map(int, input().split(" "))
    shape[1][idx] = (m, k)


def get_mult_cost(m1: tuple, m2: tuple):
    assert m1[1] == m2[0]
    return m1[0] * m1[1] * m2[1]


def get_cost(len, idx):
    if costs[len][idx] != math.inf:
        return costs[len][idx]
    min_sum = math.inf
    ridx = idx + len
    shape[len][idx] = (shape[1][idx][0], shape[1][ridx - 1][1])
    if len == 2:
        cost = get_mult_cost(shape[1][idx], shape[1][idx + 1])
        costs[len][idx] = cost
        return cost

    for cidx in range(idx, ridx - 1):
        temp_cost = 0
        temp_cost += get_cost(cidx - idx + 1, idx)
        temp_cost += get_cost(ridx - cidx - 1, cidx + 1)
        temp_cost += get_mult_cost(
            shape[cidx - idx + 1][idx], shape[ridx - cidx - 1][cidx + 1]
        )
        if min_sum > temp_cost:
            min_sum = temp_cost

    costs[len][idx] = min_sum

    return min_sum


print(get_cost(N, 0))
