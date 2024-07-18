# 3:58 4:16
import sys
import heapq as pq

MAX = 9876543210

input = sys.stdin.readline

N = int(input())
M = int(input())

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split(" "))
    edges[s].append((c, e))

Start, End = map(int, input().split(" "))

visited = [False for _ in range(N + 1)]
costs = [MAX for _ in range(N + 1)]
costs[Start] = 0

nexts = []
for c, e in edges[Start]:
    pq.heappush(nexts, (c, e))


while nexts:
    cur_c, cur_e = pq.heappop(nexts)
    if visited[cur_e]:
        continue
    visited[cur_e] = True
    costs[cur_e] = cur_c

    for edge_c, next_e in edges[cur_e]:
        if visited[next_e]:
            continue
        temp_c = costs[cur_e] + edge_c
        if costs[next_e] <= temp_c:
            continue
        costs[next_e] = temp_c
        pq.heappush(nexts, (temp_c, next_e))


print(costs[End])
