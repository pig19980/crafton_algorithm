N, K = map(int, input().split(" "))
Ns = list(map(int, list(input())))
C = N - K


cost = [[0] * (N + 2) for _ in range(C + 1)]

for row in cost:
    print(cost)

for i in range(N):
    max_j = min(i + 1, C)
    print(i, max_j)
    for j in range(1, max_j):
        ncost = cost[j - 1][i - 1] * 10 + Ns[i]
        if ncost > cost[j][i - 1]:
            cost[j][i] = ncost
        else:
            cost[j][i] = cost[j][i - 1]

for row in cost:
    print(cost)
