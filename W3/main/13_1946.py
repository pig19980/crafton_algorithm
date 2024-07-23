# 10:10 11:36
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    men_rates = []
    for i in range(N):
        t1, t2 = map(int, input().split(" "))
        men_rates.append((t1, t2))
    men_rates.sort()
    cnt = 1
    max_t2 = men_rates[0][1]
    min_t2 = men_rates[0][1] + 1

    for i in range(1, N):
        if men_rates[i][1] < max_t2 and men_rates[i][1] < min_t2:
            min_t2 = men_rates[i][1]
            cnt += 1
    print(cnt)
