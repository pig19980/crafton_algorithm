# 3:27 4:39
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
M = int(input())

costs = [(None, None) for _ in range(N + 1)]
from_edges = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split(" "))
    from_edges[e].append((s, c))

S, E = map(int, input().split(" "))

costs[S] = (0, [])


def get_cost(pos) -> tuple[int, list]:
    if costs[pos][0] != None:
        return costs[pos]
    max_cost = -1
    before_roads = []
    for from_, edge_c in from_edges[pos]:
        from_c, _ = get_cost(from_)
        if max_cost < from_c + edge_c:
            max_cost = from_c + edge_c
            before_roads = [from_]
        elif max_cost == from_c + edge_c:
            before_roads.append(from_)
    costs[pos] = (max_cost, before_roads)
    return (max_cost, before_roads)


mc, br = get_cost(E)

print(mc)

cnt = len(br)
nexts = br
visited = [False for _ in range(N + 1)]
while nexts:
    next_ = nexts.pop()
    _, nnext_ = get_cost(next_)
    for nn in nnext_:
        if not visited[nn]:
            visited[nn] = True
            nexts.append(nn)
        cnt += 1

print(cnt)
