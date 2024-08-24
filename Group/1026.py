# 10:15
import sys

input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split(" ")))
B = sorted(map(int, input().split(" ")))

min_sum = 0
for i in range(N):
    min_sum += B[i] * A[N - i - 1]
print(min_sum)
