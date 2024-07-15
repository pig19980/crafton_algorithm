# 1:07 1:55
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split(" "))))


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(i, j, visited, melt_arr):
    visited[i][j] = True
    nexts = [(i, j)]
    while nexts:
        i, j = nexts.pop()
        melt_cnt = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (0 <= ni < N) and (0 <= nj < M):
                if (not visited[ni][nj]) and arr[ni][nj] != 0:
                    visited[ni][nj] = True
                    nexts.append((ni, nj))
                if arr[ni][nj] == 0:
                    melt_cnt += 1
        melt_arr[i][j] = melt_cnt


year = 0
visited = [[False for _ in range(M)] for _ in range(N)]
melt_arr = [[0 for _ in range(M)] for _ in range(N)]

while True:
    for i in range(N):
        for j in range(M):
            visited[i][j] = False

    for i in range(N):
        for j in range(M):
            melt_arr[i][j] = 0

    # check divided
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                visited[i][j] = True
                continue
            if not visited[i][j]:
                cnt += 1
                if cnt > 1:
                    break
                dfs(i, j, visited, melt_arr)

    if cnt == 0:
        year = 0
        break
    if cnt > 1:
        break
    # calculate melt
    for i in range(N):
        for j in range(M):
            arr[i][j] = max(0, arr[i][j] - melt_arr[i][j])

    year += 1

print(year)
