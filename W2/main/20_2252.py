# 12:15 12:24
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))
edges = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]


for _ in range(M):
    s, e = map(int, input().split(" "))
    edges[s].append(e)
    indegree[e] += 1


nexts = deque()
ret = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        nexts.append(i)

while len(nexts):
    cur = nexts.popleft()
    ret.append(cur)
    for next in edges[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            nexts.append(next)

for r in ret:
    print(f"{r} ", end="")
print()
