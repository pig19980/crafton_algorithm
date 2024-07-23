# 11:52 11:56
import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))
coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0
for coin in coins[::-1]:
    q = K // coin
    cnt += q
    K -= q * coin

print(cnt)
