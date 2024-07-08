EMPTY, APPLE, SNAKE = 0, 1, 2
RIGHT, DOWN, LEFT, UP, NONE = 0, 1, 2, 3, 4

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


N = int(input())

state_map = [[{"state": EMPTY, "dir": NONE} for _ in range(N)] for _ in range(N)]
state_map[0][0] = {"state": SNAKE, "dir": RIGHT}

L = int(input())
for _ in range(L):
    y, x = map(int, input().split(" "))
    state_map[y - 1][x - 1]["state"] = APPLE

# for y in range(N):
#     for x in range(N):
#         print(state_map[y][x]["state"], end=" ")
#     print()

cmds = []
K = int(input())
for _ in range(K):
    time, cmd = input().split(" ")
    cmds.append({"time": int(time), "cmd": cmd})

cur_time = 0
hy, hx = 0, 0
ty, tx = 0, 0
next_to_go = RIGHT

while True:
    cur_time += 1
    # print(cur_time)
    # print(hy, hx)
    # print(ty, tx)

    # check head
    # if cannot got next point, stop
    # else, change location of head
    nhy, nhx = hy + dy[next_to_go], hx + dx[next_to_go]
    if nhy < 0 or nhy >= N or nhx < 0 or nhx >= N:
        break
    if state_map[nhy][nhx]["state"] == SNAKE:
        break

    hy, hx = nhy, nhx

    # check cmds. change where to go
    if len(cmds) != 0 and cmds[0]["time"] == cur_time:
        if cmds[0]["cmd"] == "D":  # turn right
            next_to_go = (next_to_go + 1) % 4
        else:
            next_to_go = (next_to_go - 1) % 4
        cmds.pop(0)

    # if got apple, continue
    if state_map[hy][hx]["state"] == APPLE:
        state_map[hy][hx]["state"] == EMPTY
        state_map[hy][hx] = {"state": SNAKE, "dir": next_to_go}
        continue

    state_map[hy][hx] = {"state": SNAKE, "dir": next_to_go}

    # check tail
    nty, ntx = ty + dy[state_map[ty][tx]["dir"]], tx + dx[state_map[ty][tx]["dir"]]
    state_map[ty][tx] = {"state": EMPTY, "dir": NONE}
    ty, tx = nty, ntx

print(cur_time)
