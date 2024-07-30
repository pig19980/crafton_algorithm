# 10:09 10:35
import sys

input = sys.stdin.readline
N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split(" "))
    T.append(t)
    P.append(p)

totP = [0 for _ in range(N + 1)]
curmax = 0
for i in range(N):
    nday = i + T[i]
    if curmax < totP[i]:
        curmax = totP[i]
    if nday <= N:
        totP[nday] = max(totP[nday], curmax + P[i])

print(max(totP))
