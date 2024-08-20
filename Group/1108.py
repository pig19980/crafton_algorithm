# 50 min
import sys

input = sys.stdin.readline

nodeN = 0
namedic = dict()
from_edge: list[list] = []


def get_idx(name) -> int:
    global nodeN
    if name not in namedic:
        namedic[name] = nodeN
        from_edge.append([])
        nodeN += 1
        return nodeN - 1
    else:
        return namedic[name]


N = int(input())
for _ in range(N):
    got = input().rstrip().split(" ")
    dest_node = got[0]
    from_nodes = got[2:]
    from_idxs = []
    get_idx(dest_node)
    for from_node in from_nodes:
        from_idxs.append(get_idx(from_node))
    from_edge[get_idx(dest_node)] = from_idxs

to_edges = [[False for _ in range(nodeN)] for _ in range(nodeN)]
for dest_idx in range(nodeN):
    for from_idx in from_edge[dest_idx]:
        to_edges[from_idx][dest_idx] = True
    to_edges[dest_idx][dest_idx] = True

for mid_idx in range(nodeN):
    for from_idx in range(nodeN):
        for dest_idx in range(nodeN):
            if to_edges[from_idx][mid_idx] and to_edges[mid_idx][dest_idx]:
                to_edges[from_idx][dest_idx] = True

grades = [None for _ in range(nodeN)]


def get_grade(idx):
    if grades[idx] != None:
        return grades[idx]
    if not from_edge[idx]:
        grades[idx] = 1
        return 1
    sum = 1
    for from_idx in from_edge[idx]:
        if to_edges[idx][from_idx]:
            continue
        sum += get_grade(from_idx)
    grades[idx] = sum
    return sum


obj_node = input().rstrip()
print(get_grade(get_idx(obj_node)))
