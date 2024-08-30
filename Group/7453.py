# 10:23
import sys

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split(" "))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD.append(-(C[i] + D[j]))
AB.sort()
CD.sort()

cnt = 0
idx1, idx2 = 0, 0
Ntot = N * N
while idx1 < Ntot and idx2 < Ntot:
    if AB[idx1] < CD[idx2]:
        idx1 += 1
    elif AB[idx1] > CD[idx2]:
        idx2 += 1
    else:
        start1, start2 = idx1, idx2
        val = AB[idx1]
        while idx1 < Ntot and AB[idx1] == val:
            idx1 += 1
        while idx2 < Ntot and CD[idx2] == val:
            idx2 += 1
        cnt += (idx1 - start1) * (idx2 - start2)

print(cnt)
