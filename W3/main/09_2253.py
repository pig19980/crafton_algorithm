# 1:16 22:22
import sys

input = sys.stdin.readline
INF = 10009
sys.setrecursionlimit(10**5)


def min_x(speed):
    return speed * (speed + 1) // 2


N, M = map(int, input().split(" "))
costs = [[None for _ in range(N + 1)] for _ in range(200)]

cannot_go = []

for _ in range(M):
    cannot_go.append(int(input()))

if 2 in cannot_go:
    print(-1)
    exit()


def get_costs(before_speed, cur):
    if costs[before_speed][cur] != None:
        return costs[before_speed][cur]
    if cur == N:
        return 0

    min_cost = INF
    for gap in range(1, -2, -1):
        next_speed = before_speed + gap
        if next_speed == 0:
            continue
        if cur + next_speed in cannot_go or cur + next_speed > N:
            continue
        temp_cost = 1 + get_costs(next_speed, cur + next_speed)
        if temp_cost < min_cost:
            min_cost = temp_cost

    costs[before_speed][cur] = min_cost
    return min_cost


ret = get_costs(1, 2) + 1
if ret == INF:
    print(-1)
else:
    print(ret)
