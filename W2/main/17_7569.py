# 6:44
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatos = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split(" "))))
    tomatos.append(box)

di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]

# make group of tomato with union find
group_checked = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
tomato_next_ripen = set()


def dfs_group(i, j, k, visited):
    visited[i][j][k] = True
    nexts = [(i, j, k)]
    can_ripe = False
    next_ripe = set()
    while nexts:
        (i, j, k) = nexts.pop()
        if tomatos[i][j][k] == 1:
            can_ripe = True
        if tomatos[i][j][k] == 0:
            for l in range(6):
                ni, nj, nk = i + di[l], j + dj[l], k + dk[l]
                if (
                    (0 <= ni < H)
                    and (0 <= nj < N)
                    and (0 <= nk < M)
                    and (tomatos[ni][nj][nk] == 1)
                ):
                    next_ripe.add((i, j, k))
                    break

        for l in range(6):
            ni, nj, nk = i + di[l], j + dj[l], k + dk[l]
            if (
                (0 <= ni < H)
                and (0 <= nj < N)
                and (0 <= nk < M)
                and (not visited[ni][nj][nk])
                and (tomatos[ni][nj][nk] != -1)
            ):
                visited[ni][nj][nk] = True
                nexts.append((ni, nj, nk))

    return can_ripe, next_ripe


cannot_ripe = False

for i in range(H):
    for j in range(N):
        for k in range(M):
            # dfs and change group_checked as True
            if (tomatos[i][j][k] != -1) and (not group_checked[i][j][k]):
                can_ripe, next_ripe = dfs_group(i, j, k, group_checked)
                # if there eixist tomato cannot ripe, return -1
                if not can_ripe:
                    cannot_ripe = True
                # add tomato_group
                tomato_next_ripen.update(next_ripe)


if cannot_ripe:
    day = -1
else:
    day = 0

    while True:
        # if there is nothing to change, break
        if len(tomato_next_ripen) == 0:
            break

        day += 1
        # change tomato
        new_ripen = set()
        for i, j, k in tomato_next_ripen:
            tomatos[i][j][k] = 1

        for i, j, k in tomato_next_ripen:
            for l in range(6):
                ni, nj, nk = i + di[l], j + dj[l], k + dk[l]
                if (
                    (0 <= ni < H)
                    and (0 <= nj < N)
                    and (0 <= nk < M)
                    and (tomatos[ni][nj][nk] == 0)
                ):
                    new_ripen.add((ni, nj, nk))
        tomato_next_ripen = new_ripen


print(day)
