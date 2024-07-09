N = int(input())
arr = list(map(int, input().split(" ")))

visited = [0] * N
indexs = [0] * N
max = -1


def get_index_and_cal_gap(depth):
    global max
    if depth == N:
        gap_sum = 0
        for i in range(N - 1):
            gap_sum += abs(arr[indexs[i]] - arr[indexs[i + 1]])

        if gap_sum > max:
            max = gap_sum
        return
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        indexs[depth] = i
        get_index_and_cal_gap(depth + 1)
        visited[i] = 0


get_index_and_cal_gap(0)

print(max)
