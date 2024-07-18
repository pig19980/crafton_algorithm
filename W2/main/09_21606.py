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


visited = [False] * (N + 1)
visited[0] = True


cnt = 0

for i in range(1, N + 1):
    if inout[i] == 1:
        visited[i] = True
        for next in edges[i]:
            if inout[next] == 1:
                cnt += 1


def dfs(cur):
    nexts = [cur]
    visited[cur] = True
    insides = 0
    while len(nexts) > 0:
        cur = nexts.pop()
        for next in edges[cur]:
            if visited[next]:
                if inout[next] == 1:
                    insides += 1
                continue
            nexts.append(next)
            visited[next] = True

    return insides


for i in range(1, N + 1):
    if not visited[i]:
        insides = dfs(i)
        cnt += insides * (insides - 1)


print(cnt)
