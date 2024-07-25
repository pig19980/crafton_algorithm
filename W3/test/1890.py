import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
move_map = []
for _ in range(N):
    move_map.append(list(map(int, input().split(" "))))

cost_map = [[None for _ in range(N)] for _ in range(N)]
cost_map[N - 1][N - 1] = 1

di = [1, 0]
dj = [0, 1]


def get_cost(i, j):
    if cost_map[i][j] != None:
        return cost_map[i][j]
    cost = 0
    if move_map[i][j] == 0:
        cost_map[i][j] = 0
        return 0
    for k in range(2):
        ni, nj = i + di[k] * move_map[i][j], j + dj[k] * move_map[i][j]
        if (0 <= ni < N) and (0 <= nj < N):
            cost += get_cost(ni, nj)
    cost_map[i][j] = cost
    return cost


get_cost(N // 2, N // 2)
get_cost(N // 2, 0)
get_cost(0, N // 2)

print(get_cost(0, 0))
