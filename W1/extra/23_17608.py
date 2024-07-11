# 8:24

import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

min = -1
cnt = 0
for elem in arr[::-1]:
    if elem > min:
        cnt += 1
        min = elem
print(cnt)
