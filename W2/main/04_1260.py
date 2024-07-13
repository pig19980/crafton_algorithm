# 10:20

import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split(" "))
costs = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split(" "))
    costs[s][e] = 1
    costs[e][s] = 1

# for row in costs:
#     print(row)


visited = [0] * (N + 1)


def DFS(cur):
    visited[cur] = 1
    print(f"{cur} ", end="")
    for next in range(1, N + 1):
        if costs[cur][next] == 1 and visited[next] == 0:
            DFS(next)


DFS(V)
print()

visited = [0] * (N + 1)


def BFS(start):
    next_que = deque()
    next_que.append(start)
    visited[start] = 1
    while len(next_que) > 0:
        cur = next_que.popleft()
        print(f"{cur} ", end="")

        for next in range(1, N + 1):
            if costs[cur][next] == 1 and visited[next] == 0:
                next_que.append(next)
                visited[next] = 1


BFS(V)
print()
