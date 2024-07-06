import random

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))


def swap(i1, i2):
    t = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = t


def qsort(li, ri):
    if li >= ri:
        return
    # print("input", li, ri, arr)

    pi = random.randrange(li, ri + 1)
    swap(li, pi)

    pv = arr[li]
    lp = li
    rp = ri

    while lp < rp:
        # swap
        while arr[lp] <= pv and lp < rp:
            lp += 1
        while arr[rp] > pv and lp < rp:
            rp -= 1

        if lp <= rp:
            swap(lp, rp)
        # print(lp, rp, arr)

    if arr[rp] > pv:
        swap(rp - 1, li)
        rp = rp - 1
    else:
        swap(rp, li),

    # print("output", arr)
    qsort(li, rp - 1)
    qsort(rp + 1, ri)


# arr.sort()
qsort(0, len(arr) - 1)


for elem in arr:
    print(elem)
