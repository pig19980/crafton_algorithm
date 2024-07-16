# 13:14
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N + 1)]

while True:
    try:
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)
    except:
        break

pnodes = [0] * (N + 1)
nexts = deque()
nexts.append(1)
pnodes[1] = -1

while len(nexts) > 0:
    cur = nexts.popleft()
    for next in edges[cur]:
        if pnodes[next] == 0:
            pnodes[next] = cur
            nexts.append(next)

# print(pnodes)
for i in pnodes[2 : N + 1]:
    print(i)
