import sys

input = sys.stdin.readline

M, N, L = map(int, input().split(" "))
mans = list(map(int, input().split(" ")))
animals = []
for _ in range(N):
    x, y = map(int, input().split(" "))
    animals.append((x, y))

mans.sort()

cnt = 0

for x, y in animals:
    can_catch = False
    # check can catch
    lp, rp = 0, M - 1
    while True:
        mid = (lp + rp) // 2
        if mans[mid] + L < x + y:
            lp = mid + 1
        elif L - mans[mid] < -x + y:
            rp = mid - 1
        else:
            can_catch = True
            break

        if lp > rp:
            break

    if can_catch:
        cnt += 1

print(cnt)
