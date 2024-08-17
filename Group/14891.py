# 10:32 11:15
from collections import deque
import sys

input = sys.stdin.readline

DIR12 = 0
DIRRIGHT = 2
DIRLEFT = 6

cogwheels = []
for _ in range(4):
    cogwheels.append(deque(map(int, input().rstrip())))


def rot(cogwheel: deque, rot_dir):
    if rot_dir == 1:
        end = cogwheel.pop()
        cogwheel.appendleft(end)
    else:
        front = cogwheel.popleft()
        cogwheel.append(front)


def rot_propa(cog_idx, rot_dir, propa_dir):
    if propa_dir == 1:
        if cog_idx + 1 < 4:
            if cogwheels[cog_idx][DIRRIGHT] != cogwheels[cog_idx + 1][DIRLEFT]:
                rot_propa(cog_idx + 1, -rot_dir, propa_dir)
        rot(cogwheels[cog_idx], rot_dir)
    else:
        if cog_idx - 1 >= 0:
            if cogwheels[cog_idx][DIRLEFT] != cogwheels[cog_idx - 1][DIRRIGHT]:
                rot_propa(cog_idx - 1, -rot_dir, propa_dir)
        rot(cogwheels[cog_idx], rot_dir)


N = int(input())
for _ in range(N):
    idx, rot_dir = map(int, input().split(" "))
    idx -= 1
    rot_propa(idx, rot_dir, 1)
    rot(cogwheels[idx], -rot_dir)
    rot_propa(idx, rot_dir, -1)


sum = 0
tsum = 1
for cog in cogwheels:
    sum += cog[DIR12] * tsum
    tsum <<= 1
print(sum)
