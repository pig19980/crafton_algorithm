# 2:48 2:58
# 3:19 3:23
import sys
from collections import deque

MAX = 9876543210

input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))

costs = [[MAX for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

costs[0][0] = 1
visited[0][0] = True
nexts = deque()
nexts.append((0, 0))

while nexts:
    ci, cj = nexts.popleft()
    cur_cost = costs[ci][cj]

    if (ci, cj) == (N - 1, M - 1):
        break

    for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]
        if (0 <= ni < N) and (0 <= nj < M) and arr[ni][nj] == 1 and not visited[ni][nj]:
            nexts.append((ni, nj))
            visited[ni][nj] = True
            costs[ni][nj] = cur_cost + 1

print(costs[N - 1][M - 1])
