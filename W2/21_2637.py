# 12:54 13:05
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

indegrees = [0 for _ in range(N + 1)]
costs = [-1 for _ in range(N + 1)]
costs[N] = 1

upper_edge = [[] for _ in range(N + 1)]

for _ in range(M):
    X, Y, K = map(int, input().split(" "))
    indegrees[X] += 1
    upper_edge[Y].append((X, K))

basic_device = []

for i in range(1, N + 1):
    if indegrees[i] == 0:
        basic_device.append(i)


def get_cost(dev):
    if costs[dev] != -1:
        return costs[dev]
    sum = 0
    for x, k in upper_edge[dev]:
        sum += get_cost(x) * k
    costs[dev] = sum
    return sum


for bd in basic_device:
    bd_cost = get_cost(bd)
    if bd_cost > 0:
        print(bd, bd_cost)
