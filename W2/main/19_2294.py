# 10:05 11:14
import sys

MAX = -1

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split(" "))
coins = []
for _ in range(N):
    coin = int(input())
    if coin < K:
        coins.append(coin)
    elif coin == K:
        print(1)
        exit()


costs = [MAX for _ in range(K + 1)]
costs[0] = 0

coins = list(set(coins))
coins.sort()


for coin in coins:
    costs[coin] = 1


def get_cost(k):
    if k < 0:
        return MAX
    if costs[k] != MAX:
        return costs[k]
    min_cost = MAX
    for i in range(len(coins)):
        if k - coins[i] < 0:
            break
        before_cost = get_cost(k - coins[i])
        if before_cost == MAX:
            continue
        temp_cost = before_cost + 1
        if temp_cost < min_cost or min_cost == MAX:
            min_cost = temp_cost

    costs[k] = min_cost
    return min_cost


ret = get_cost(K)
if ret == MAX:
    print(-1)
else:
    print(ret)
