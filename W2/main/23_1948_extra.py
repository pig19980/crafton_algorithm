import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

costs = [(None, None) for _ in range(N + 1)]
from_edges = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split(" "))
    from_edges[e].append((s, c))

S, E = map(int, input().split(" "))

next_dp = [E]
visited_dp = [False for _ in range(N + 1)]

costs[S] = (0, [])
visited_dp[S] = True

# not using recursion version
# if need more improve, use topological sorting
# and update from last index
while next_dp:
    pos = next_dp.pop()
    if costs[pos][0] != None:
        continue

    if not visited_dp[pos]:
        next_dp.append(pos)
        for from_, _ in from_edges[pos]:
            next_dp.append(from_)
        visited_dp[pos] = True
        continue

    max_cost = -1
    before_roads = []
    for from_, edge_c in from_edges[pos]:
        from_c, _ = costs[from_]
        if max_cost < from_c + edge_c:
            max_cost = from_c + edge_c
            before_roads = [from_]
        elif max_cost == from_c + edge_c:
            before_roads.append(from_)
    costs[pos] = (max_cost, before_roads)


mc, br = costs[E]

print(mc)

cnt = len(br)
nexts = br
visited = [False for _ in range(N + 1)]
while nexts:
    next_ = nexts.pop()
    _, nnext_ = costs[next_]
    for nn in nnext_:
        if not visited[nn]:
            visited[nn] = True
            nexts.append(nn)
        cnt += 1

print(cnt)
