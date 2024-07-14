import sys

input = sys.stdin.readline

T = int(input())


def check_bin(graph, visited, pos):
    nexts = []
    nexts.append(pos)
    color[pos] = 1
    visited[pos] = True

    while len(nexts) > 0:
        cur = nexts.pop()
        for next in graph[cur]:
            if not visited[next]:
                color[next] = color[cur] * -1
                nexts.append(next)
                visited[next] = True
            else:
                if color[cur] == color[next]:
                    return False

    return True


for _ in range(T):
    V, E = map(int, input().split(" "))
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    visited[0] = True
    color = [0] * (V + 1)

    for _ in range(E):
        s, e = map(int, input().split(" "))
        graph[s].append(e)
        graph[e].append(s)

    # for row in graph:
    #     print(row)

    checked = False
    # print(visited)
    is_bin = True
    while not checked:
        checked = True
        for i in range(1, V + 1):
            if visited[i] == False:
                is_bin = check_bin(graph, visited, i)
                if is_bin == False:
                    break

    if is_bin:
        print("YES")
    else:
        print("NO")
