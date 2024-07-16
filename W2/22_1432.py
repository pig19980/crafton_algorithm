# 1:13 1:49
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
edges = [[] for _ in range(N)]
indegrees = [0 for _ in range(N)]
for i in range(N):
    got = list(map(int, input().strip()))
    for j in range(N):
        if got[j] == 1:
            edges[j].append(i)
            indegrees[i] += 1


nexts = []
for i in range(N):
    if indegrees[i] == 0:
        heappush(nexts, -i)
ret = [None for _ in range(N)]
curNum = N


while nexts:
    curIdx = -heappop(nexts)
    ret[curIdx] = curNum
    curNum -= 1

    for next in edges[curIdx]:
        indegrees[next] -= 1
        if indegrees[next] == 0:
            heappush(nexts, -next)


for i in indegrees:
    if indegrees[i] > 0:
        print(-1)
        exit()

for elem in ret:
    print(f"{elem} ", end="")
print()
