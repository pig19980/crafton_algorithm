import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

cash = arr.copy()


def msort(l, r):
    if l + 1 >= r:
        return

    mid = (l + r) // 2
    msort(l, mid)
    msort(mid, r)

    li, ri, ci = l, mid, l
    while li < mid and ri < r:
        if cash[li] < cash[ri]:
            arr[ci] = cash[li]
            li += 1
        else:
            arr[ci] = cash[ri]
            ri += 1
        ci += 1

    if li != mid:
        arr[ci:r] = cash[li:mid]
    else:
        arr[ci:r] = cash[ri:r]

    cash[l:r] = arr[l:r]


msort(0, len(arr))


for elem in arr:
    print(elem)
