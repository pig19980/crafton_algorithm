# 1 hour
import sys

input = sys.stdin.readline

LOCY = 0
LOCX = 1
DIR = 2

N, K = map(int, input().split(" "))
color_map = []
chess_map = [[[] for _ in range(N)] for _ in range(N)]
chess_state = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    color_map.append(list(map(int, input().split(" "))))
for chess_idx in range(K):
    y, x, dir = map(int, input().split(" "))
    chess_state.append([y - 1, x - 1, dir - 1])
    chess_map[y - 1][x - 1].append(chess_idx)


def update_chess():
    for chess_idx in range(K):
        cy, cx, dir = chess_state[chess_idx]
        # update location
        ncy, ncx = cy + dy[dir], cx + dx[dir]
        if not (0 <= ncy < N) or not (0 <= ncx < N) or color_map[ncy][ncx] == 2:
            ncy, ncx = cy, cx
            if dir % 2 == 0:
                chess_state[chess_idx][DIR] += 1
            else:
                chess_state[chess_idx][DIR] -= 1
            dir = chess_state[chess_idx][DIR]

            ncy, ncx = cy + dy[dir], cx + dx[dir]
            if not (0 <= ncy < N) or not (0 <= ncx < N) or color_map[ncy][ncx] == 2:
                ncy, ncx = cy, cx
        if (ncy, ncx) == (cy, cx):
            continue
        temp_idx = chess_map[cy][cx].index(chess_idx)
        chess_map[cy][cx], moving_chess = chess_map[cy][cx][:temp_idx], chess_map[cy][cx][temp_idx:]
        if color_map[ncy][ncx] == 1:
            moving_chess.reverse()
        chess_map[ncy][ncx].extend(moving_chess)
        if len(chess_map[ncy][ncx]) >= 4:
            return False
        for moved_chess_idx in moving_chess:
            chess_state[moved_chess_idx][LOCY] = ncy
            chess_state[moved_chess_idx][LOCX] = ncx

    return True


cnt = 0
while cnt <= 1000:
    cnt += 1
    if update_chess():
        continue
    else:
        break

if cnt > 1000:
    print(-1)
else:
    print(cnt)
