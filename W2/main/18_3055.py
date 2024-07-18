# 10:25 10:56
import sys
from collections import deque

MAX = 9876543210
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

input = sys.stdin.readline

R, C = map(int, input().split(" "))
forest_map = []
for _ in range(R):
    forest_map.append(input().strip())

floor_map = [[MAX for _ in range(C)] for _ in range(R)]
go_map = [[MAX for _ in range(C)] for _ in range(R)]

S, D = None, None

next_floor = deque()
for i in range(R):
    for j in range(C):
        if forest_map[i][j] == "D":
            D = (i, j)
        elif forest_map[i][j] == "S":
            S = (i, j)
        elif forest_map[i][j] == "*":
            next_floor.append((i, j))
            floor_map[i][j] = 0

while next_floor:
    ci, cj = next_floor.popleft()
    cur_cost = floor_map[ci][cj]

    for k in range(4):
        ni, nj = ci + di[k], cj + dj[k]
        if (
            0 <= ni < R
            and 0 <= nj < C
            and forest_map[ni][nj] in (".", "S")
            and floor_map[ni][nj] == MAX
        ):
            floor_map[ni][nj] = cur_cost + 1
            next_floor.append((ni, nj))


next_go = deque()
next_go.append(S)
go_map[S[0]][S[1]] = 0

while next_go:
    ci, cj = next_go.popleft()
    cur_cost = go_map[ci][cj]

    for k in range(4):
        ni, nj = ci + di[k], cj + dj[k]
        if (
            0 <= ni < R
            and 0 <= nj < C
            and forest_map[ni][nj] in (".", "D")
            and cur_cost + 1 < floor_map[ni][nj]
            and cur_cost + 1 < go_map[ni][nj]
        ):
            go_map[ni][nj] = cur_cost + 1
            next_go.append((ni, nj))

ret = go_map[D[0]][D[1]]
if ret == MAX:
    print("KAKTUS")
else:
    print(ret)
