import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

house_map = []
for _ in range(N):
    house_map.append(list(map(int, input().strip())))

cnt_list = []
visited = [[False for _ in range(N)] for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


for i in range(N):
    for j in range(N):
        if visited[i][j] or house_map[i][j] == 0:
            continue
        cnt = 1
        nexts = deque()
        nexts.append((i, j))
        visited[i][j] = True
        while nexts:
            ci, cj = nexts.popleft()

            for k in range(4):
                ni, nj = ci + di[k], cj + dj[k]
                if (
                    0 <= ni < N
                    and 0 <= nj < N
                    and not visited[ni][nj]
                    and house_map[ni][nj] == 1
                ):
                    cnt += 1
                    visited[ni][nj] = True
                    nexts.append((ni, nj))

        cnt_list.append(cnt)


cnt_list.sort()
print(len(cnt_list))
for cnt in cnt_list:
    print(cnt)
