# 12:31 12:40
import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))
ws, vs = [], []
for _ in range(N):
    w, v = map(int, input().split(" "))
    ws.append(w)
    vs.append(v)

costs = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for n in range(N):
    for w in range(K + 1):
        if w - ws[n] >= 0:
            costs[n + 1][w] = max(costs[n][w], costs[n][w - ws[n]] + vs[n])
        else:
            costs[n + 1][w] = costs[n][w]

print(costs[N][K])
