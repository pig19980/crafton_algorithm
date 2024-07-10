import sys

input = sys.stdin.readline


def check_area_ok(arr, maxH, A):
    print("got area", A)
    maxH = min(maxH, A)
    lH, rH = 1, maxH
    while True:
        midH = (lH + rH + 1) // 2
        minN = (A + midH - 1) // midH
        print(midH, minN)

        # H should higher
        if minN > len(arr):
            lH = midH + 1
            if lH > rH:
                break
            continue

        cnt = 0
        for h in arr:
            if h >= midH:
                cnt += 1
            else:
                cnt = 0

            if cnt == minN:
                break

        if cnt == minN:
            return True

        # H should shorter
        rH = midH - 1
        if lH > rH:
            break

    return False


while True:
    got = input().split(" ")
    print(got)
    if len(got) == 1:
        break
    arr = list(map(int, got))
    N = arr[0]
    arr = arr[1:]
    print(N, arr)

    maxH = max(arr)
    maxArea = N * maxH

    lA, rA = 1, maxArea

    # find upper bound of area
    while True:
        midA = (lA + rA + 1) // 2
        if check_area_ok(arr, maxH, midA):
            rA = midA
        else:
            lA = midA + 1

        if lA == rA:
            break

    print(rA)
