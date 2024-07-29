# 10:21 11:11
import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))
coins = []
for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)

cnts = [0 for _ in range(K + 1)]

cnts[0] = 1

for i in range(len(coins)):
    for j in range(coins[i], K + 1):
        cnts[j] += cnts[j - coins[i]]

print(cnts[K])
