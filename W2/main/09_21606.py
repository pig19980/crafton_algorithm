# 8:16

import sys

input = sys.stdin.readline

N = int(input())
inout = [0] + list(map(int, input().strip()))
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split(" "))
    edges[s].append(e)
    edges[e].append(s)


cnt = 0

for i in range(1, N + 1):
    if len(edges[i]) > 0:
        # dfs from i
        ins = 0
        nexts = []
        nexts[i] = True
        for next in edges[i]:
            nexts.append(next)
            visited[next] = True
        if inout[i] == 1:
            ins += 1

        while len(nexts) > 0:
            cur = nexts.pop()
            if inout[cur] == 1:
                ins += 1
                continue

            for next in edges[cur]:
                if not visited[next]:
                    visited[next] = True
                    nexts.append(next)

        # print(ins)
        cnt += ins * (ins - 1)

print(cnt)
