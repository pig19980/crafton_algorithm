N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split(" "))))

visited = [False] * N
min_cost = 987654321


def get_min(cur, level, cur_cost):
    global min_cost
    # print(cur, level, cur_cost)

    if level == N and W[cur][0] != 0:
        cost = cur_cost + W[cur][0]
        if cost < min_cost:
            min_cost = cost

    for i in range(N):
        if visited[i] or W[cur][i] == 0:
            continue
        visited[i] = True
        get_min(i, level + 1, cur_cost + W[cur][i])
        visited[i] = False


visited[0] = True
get_min(0, 1, 0)
print(min_cost)
