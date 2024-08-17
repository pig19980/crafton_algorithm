# 10:06
import sys
from collections import deque


input = sys.stdin.readline
R, C, N = map(int, input().split(" "))


def check_same_mat(mat1, mat2, R, C):
    for i in range(R):
        for j in range(C):
            if mat1[i][j] != mat2[i][j]:
                return False
    return True


bomb_map = []
di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

for _ in range(R):
    bomb_map.append(list(input().rstrip()))

bomb_map_blocks = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(4)]
for i in range(R):
    for j in range(C):
        if bomb_map[i][j] == "O":
            bomb_map_blocks[1][i][j] = 2


t = 2
while t <= N:
    before_bomb_map = bomb_map_blocks[(t - 1) % 4]
    cur_bomb_map = bomb_map_blocks[t % 4]
    temp_bomb_map = [[None for _ in range(C)] for _ in range(R)]
    stack = []
    for i in range(R):
        for j in range(C):
            temp_bomb_map[i][j] = before_bomb_map[i][j] + 1
            if temp_bomb_map[i][j] == 4:
                stack.append((i, j))
    while stack:
        i, j = stack.pop()
        temp_bomb_map[i][j] = 0
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                temp_bomb_map[ni][nj] = 0

    if t > 4 and check_same_mat(cur_bomb_map, temp_bomb_map, R, C):
        break
    for i in range(R):
        for j in range(C):
            cur_bomb_map[i][j] = temp_bomb_map[i][j]

    t += 1

cur_bomb_map = bomb_map_blocks[N % 4]

for row in cur_bomb_map:
    rowout = "".join(map(lambda x: "." if (x == 0) else "O", row))
    print(rowout)
