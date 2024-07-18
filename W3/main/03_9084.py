# 11:07 12:10
import sys

input = sys.stdin.readline


def get_cost(costs, coins, n, m):
    if n == 0 or m < 0:
        return 0
    if n == 1:
        if m % coins[0] == 0:
            costs[0][m] = 1
            return 1
        else:
            costs[0][m] = 0
            return 0
    if costs[n - 1][m] != None:
        return costs[n - 1][m]
    sum = 0
    curm = m
    while curm > 0:
        sum += get_cost(costs, coins, n - 1, curm)
        curm -= coins[n - 1]
    if m % coins[n - 1] == 0:
        sum += 1
    costs[n - 1][m] = sum
    return sum


T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split(" ")))
    M = int(input())
    costs = [[None for _ in range(M + 1)] for _ in range(len(coins))]
    for row in costs:
        row[0] = 1
    cost = get_cost(costs, coins, N, M)

    print(cost)
