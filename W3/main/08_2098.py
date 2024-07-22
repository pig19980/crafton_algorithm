# 4:15 5:30
import sys

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
road_map = []
for _ in range(N):
    road_map.append(list(map(int, input().split(" "))))

costs = [[None for _ in range(2**N)] for _ in range(N)]


def get_idx(arr):
    ret = arr[0]
    for elem in arr[1:]:
        ret = ret * 2 + elem
    return ret


nexts = [0 for _ in range(4)]
nexts[0] = 1


# from 0, visit nexts, and last go to cur
def get_costs(cur, nexts):
    idx = get_idx(nexts)
    if costs[cur][idx] != None:
        return costs[cur][idx]

    next_name = []
    for i in range(N):
        if nexts[i] == 0:
            next_name.append(i)
    if len(next_name) == 0:
        ret = road_map[0][cur]
        if ret == 0:
            ret = INF
        costs[cur][idx] = ret
        return ret

    min_ret = INF
    for next_idx in next_name:
        if road_map[next_idx][cur] == 0:
            continue
        nexts[next_idx] = 1
        temp_ret = get_costs(next_idx, nexts) + road_map[next_idx][cur]
        if min_ret > temp_ret:
            min_ret = temp_ret
        nexts[next_idx] = 0
    costs[cur][idx] = min_ret
    return min_ret


nexts = [0 for _ in range(N)]
nexts[0] = 1
print(get_costs(0, nexts))
