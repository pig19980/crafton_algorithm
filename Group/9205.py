# 10:13 10:31
import sys

input = sys.stdin.readline


def get_dist(p1: tuple, p2: tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


T = int(input())
for _ in range(T):
    N = int(input())
    points = []  # len is N + 2. points[0] is start, points[N+1] is dest
    points.append(tuple(map(int, input().split(" "))))
    for _ in range(N):
        points.append(tuple(map(int, input().split(" "))))
    points.append(tuple(map(int, input().split(" "))))

    cost_map = [[None for _ in range(N + 2)] for _ in range(N + 2)]
    for i in range(N + 2):
        for j in range(i, N + 2):
            if i == j:
                cost_map[i][j] = 0
                continue
            cost = get_dist(points[i], points[j])
            cost_map[i][j] = cost
            cost_map[j][i] = cost

    visited = [False for _ in range(N + 2)]
    visited[0] = True
    nexts = [0]
    while nexts:
        cur = nexts.pop()
        for next in range(N + 2):
            if not visited[next] and cost_map[cur][next] <= 1000:
                visited[next] = True
                nexts.append(next)
    if visited[N + 1]:
        print("happy")
    else:
        print("sad")
