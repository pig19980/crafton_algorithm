import sys
from heapq import heappop, heappush

input = sys.stdin.readline

virus_map = []
N, K = map(int, input().split(" "))

for _ in range(N):
    virus_map.append(list(map(int, input().split(" "))))


S, X, Y = map(int, input().split(" "))
X -= 1
Y -= 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

if S == 0:
    print(virus_map[X][Y])
    exit()


def check_near(i, j):
    ret = []
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and virus_map[ni][nj] == 0:
            ret.append((ni, nj))
    return ret


nexts = []
for i in range(N):
    for j in range(N):
        if virus_map[i][j] != 0:
            v_name = virus_map[i][j]
            if check_near(i, j):
                heappush(nexts, (v_name, i, j))
                virus_map[i][j] = 0

cur_T = -1
while cur_T < S:
    nnexts = []
    while nexts:
        cv, ci, cj = heappop(nexts)
        if virus_map[ci][cj] != 0:
            continue
        virus_map[ci][cj] = cv

        for ni, nj in check_near(ci, cj):
            heappush(nnexts, (cv, ni, nj))

    cur_T += 1
    nexts = nnexts

print(virus_map[X][Y])
