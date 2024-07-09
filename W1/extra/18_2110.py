import sys

input = sys.stdin.readline

N, C = map(int, input().split(" "))
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()


def maxC(minGap):
    ret = 1
    before = houses[0]
    for i in range(1, N):
        if houses[i] - before >= minGap:
            ret += 1
            before = houses[i]
    return ret


l, r = 0, 1000000000
while True:
    mid = (l + r + 1) // 2
    if maxC(mid) >= C:
        l = mid
    else:
        r = mid - 1

    if l == r:
        break

print(l)
