# 3:38 3:54
import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split(" "))

edges = [[] for _ in range(N + 1)]
costs = [None for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split(" "))
    edges[s].append(e)

nexts = deque()
nexts.append(X)
costs[X] = 0
visited[X] = True

ret = []

while nexts:
    cur = nexts.popleft()
    cur_cost = costs[cur]

    if cur_cost == K:
        ret.append(cur)
        continue

    for next in edges[cur]:
        if not visited[next]:
            nexts.append(next)
            visited[next] = True
            costs[next] = cur_cost + 1

ret.sort()

if len(ret) == 0:
    print(-1)
else:
    for e in ret:
        print(e)
