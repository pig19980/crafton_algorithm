# 3 hour
import sys
from collections import deque

namedic = {
    "U": 0,
    "D": 1,
    "F": 2,
    "B": 3,
    "L": 4,
    "R": 5,
}
centor_color = ("w", "y", "r", "o", "g", "b")
edge_color: list[deque] = []


roted_sruface = (
    ((2, 5, 3, 4), ((0, 1, 2), (0, 1, 2), (0, 1, 2), (0, 1, 2))),
    ((2, 4, 3, 5), ((4, 5, 6), (4, 5, 6), (4, 5, 6), (4, 5, 6))),
    ((0, 4, 1, 5), ((4, 5, 6), (2, 3, 4), (4, 5, 6), (6, 7, 0))),
    ((0, 5, 1, 4), ((0, 1, 2), (2, 3, 4), (0, 1, 2), (6, 7, 0))),
    ((0, 3, 1, 2), ((6, 7, 0), (2, 3, 4), (2, 3, 4), (6, 7, 0))),
    ((0, 2, 1, 3), ((2, 3, 4), (2, 3, 4), (6, 7, 0), (6, 7, 0))),
)


def rot_surface(surDir, rotDir):
    surIdx = namedic[surDir]
    if rotDir == "-":
        edge_color[surIdx].rotate(-2)
        roted_surIdx = roted_sruface[surIdx][0]
        roted_dqIdx = roted_sruface[surIdx][1]
        for i in range(3):
            (
                edge_color[roted_surIdx[0]][roted_dqIdx[0][i]],
                edge_color[roted_surIdx[1]][roted_dqIdx[1][i]],
                edge_color[roted_surIdx[2]][roted_dqIdx[2][i]],
                edge_color[roted_surIdx[3]][roted_dqIdx[3][i]],
            ) = (
                edge_color[roted_surIdx[3]][roted_dqIdx[3][i]],
                edge_color[roted_surIdx[0]][roted_dqIdx[0][i]],
                edge_color[roted_surIdx[1]][roted_dqIdx[1][i]],
                edge_color[roted_surIdx[2]][roted_dqIdx[2][i]],
            )

    else:
        edge_color[surIdx].rotate(2)
        roted_surIdx = roted_sruface[surIdx][0]
        roted_dqIdx = roted_sruface[surIdx][1]
        for i in range(3):
            (
                edge_color[roted_surIdx[0]][roted_dqIdx[0][i]],
                edge_color[roted_surIdx[1]][roted_dqIdx[1][i]],
                edge_color[roted_surIdx[2]][roted_dqIdx[2][i]],
                edge_color[roted_surIdx[3]][roted_dqIdx[3][i]],
            ) = (
                edge_color[roted_surIdx[1]][roted_dqIdx[1][i]],
                edge_color[roted_surIdx[2]][roted_dqIdx[2][i]],
                edge_color[roted_surIdx[3]][roted_dqIdx[3][i]],
                edge_color[roted_surIdx[0]][roted_dqIdx[0][i]],
            )


def print_surface(surIdx):
    print(f"{edge_color[surIdx][0]}{edge_color[surIdx][1]}{edge_color[surIdx][2]}")
    print(f"{edge_color[surIdx][7]}{centor_color[surIdx]}{edge_color[surIdx][3]}")
    print(f"{edge_color[surIdx][6]}{edge_color[surIdx][5]}{edge_color[surIdx][4]}")


input = sys.stdin.readline
testN = int(input())
for _ in range(testN):
    edge_color = []
    for c in centor_color:
        edge_color.append(deque([c for _ in range(8)]))

    cmdN = int(input())
    cmds = (input().rstrip()).split(" ")
    for cmd in cmds:
        rot_surface(cmd[0], cmd[1])
    print_surface(0)
