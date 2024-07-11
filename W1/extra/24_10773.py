# 8:36
import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
stack = []

for _ in range(K):
    got = int(input())
    if got == 0:
        if len(stack) != 0:
            stack.pop()
        continue
    stack.append(got)

sum = 0
for e in stack:
    sum += e
print(sum)
