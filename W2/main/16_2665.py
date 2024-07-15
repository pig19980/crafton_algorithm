# 4:20 4:42
import sys, heapq

MAX = 9876543210
input = sys.stdin.readline

N = int(input())
arr_map = []
for _ in range(N):
    arr_map.append(list(map(int, input().strip())))

costs = [[MAX for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


nexts = [(0, 0, 0)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while nexts:
    cc, ci, cj = heapq.heappop(nexts)
    if visited[ci][cj]:
        continue
    visited[ci][cj] = True
    costs[ci][cj] = cc

    for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]
        if (0 <= ni < N) and (0 <= nj < N) and not visited[ni][nj]:
            nc = cc + 1 - arr_map[ni][nj]
            heapq.heappush(nexts, (nc, ni, nj))


print(costs[N - 1][N - 1])
