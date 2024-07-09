# solve by dp

N = int(input())
arr = list(map(int, input().split(" ")))
costs = [[0] * 1001 for _ in range(1001)]
for i in range(1001):
    costs[i][-1] = -1

for n in range(0, N):
    for cnt in range(n + 1):
        if costs[n - 1][cnt - 1] != 0 and arr[n] > costs[n - 1][cnt - 1]:
            new_cost = arr[n]
            if costs[n - 1][cnt] > new_cost or costs[n - 1][cnt] == 0:
                costs[n][cnt] = new_cost
            else:
                costs[n][cnt] = costs[n - 1][cnt]
        else:
            costs[n][cnt] = costs[n - 1][cnt]

        if costs[n][cnt] == 0:
            break


cnt = 0
for elem in costs[N - 1]:
    if elem in (0, -1):
        break
    cnt += 1
print(cnt)
