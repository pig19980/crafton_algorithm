N, S = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

cur_sum = 0
cnt = 0

if S == 0:
    cnt -= 1


def check_sum(idx):
    global arr, cur_sum, cnt, N
    if idx == N:
        if cur_sum == S:
            cnt += 1
        return

    cur_sum += arr[idx]
    check_sum(idx + 1)
    cur_sum -= arr[idx]
    check_sum(idx + 1)


check_sum(0)
print(cnt)
