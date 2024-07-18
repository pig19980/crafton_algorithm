import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))

tile_map = []
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    got = list(input().strip())
    tile_map.append(got)


cnt = 0

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]


for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        cnt += 1
        # run bfs
        nexts = deque()
        nexts.append((i, j))
        visited[i][j] = True

        while nexts:
            ci, cj = nexts.popleft()
            cur_tile = tile_map[ci][cj]
            if cur_tile == "-":
                for k in range(0, 2):
                    ni, nj = ci + di[k], cj + dj[k]
                    if (
                        0 <= ni < N
                        and 0 <= nj < M
                        and tile_map[ni][nj] == cur_tile
                        and not visited[ni][nj]
                    ):
                        visited[ni][nj] = True
                        nexts.append((ni, nj))
            else:
                for k in range(2, 4):
                    ni, nj = ci + di[k], cj + dj[k]
                    if (
                        0 <= ni < N
                        and 0 <= nj < M
                        and tile_map[ni][nj] == cur_tile
                        and not visited[ni][nj]
                    ):
                        visited[ni][nj] = True
                        nexts.append((ni, nj))

print(cnt)
