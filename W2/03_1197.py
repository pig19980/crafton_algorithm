# 7:20 ~ 7:37
import heapq


V, E = map(int, input().split(" "))

edges = []
union = [0] * (V + 1)

for _ in range(E):
    s, e, c = map(int, input().split(" "))
    heapq.heappush(edges, (c, s, e))


def get_top(p):
    cur = p
    while union[cur] != cur:
        cur = union[cur]
    union[p] = cur
    return cur


tot_cost = 0

while len(edges) > 0:
    (c, s, e) = heapq.heappop(edges)
    s_top = get_top(s)
    e_top = get_top(e)
    if s_top == e_top and s_top != 0:
        continue
    if s_top == 0 and e_top == 0:
        union[s], union[e] = s, s
    elif s_top == 0:
        union[s] = e_top
    elif e_top == 0:
        union[e] = s_top
    else:
        union[e_top] = s_top

    tot_cost += c
    print(union)

print(tot_cost)
