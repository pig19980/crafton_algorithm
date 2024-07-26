# 10:05 10:12
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    before = list(range(1, n + 1))
    for _ in range(k):
        current = []
        for i in range(n):
            current.append(sum(before[: i + 1]))
        before = current
    print(before[n - 1])
