from collections import deque

N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split(" "))))

visited = [[False] * N for _ in range(N)]
max_cnt = -1


def print_visited():
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                print("T ", end="")
            else:
                print("F ", end="")
        print()
    print()


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


for flooded in range(101):
    all_flooded = True
    cur_cnt = 0
    for i in range(N):
        for j in range(N):
            # if here is not visited and flooded, cnt++
            if W[i][j] > flooded and not visited[i][j]:
                cur_cnt += 1
                all_flooded = False

                # update nearby as visited
                next_queue = deque()
                next_queue.append((i, j))
                visited[i][j] = True

                while len(next_queue) > 0:
                    ci, cj = next_queue.popleft()

                    for k in range(4):
                        ni = ci + di[k]
                        nj = cj + dj[k]
                        if (
                            (0 <= ni < N)
                            and (0 <= nj < N)
                            and W[ni][nj] > flooded
                            and not visited[ni][nj]
                        ):
                            next_queue.append((ni, nj))
                            visited[ni][nj] = True

                # print_visited()

    # print(flooded, cur_cnt)
    # update max_cnt
    if cur_cnt > max_cnt:
        max_cnt = cur_cnt
    # if all region is flooded, stop searching
    if all_flooded:
        break

    # reset visited
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

print(max_cnt)
