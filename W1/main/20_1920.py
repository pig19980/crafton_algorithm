N = int(input())
A = list(map(int, input().split(" ")))
M = int(input())
check_list = list(map(int, input().split(" ")))

A.sort()

for c in check_list:
    # bin search
    pl, pr = 0, len(A)
    found = False
    while pl < pr:
        mid = (pl + pr) // 2
        if A[mid] == c:
            found = True
            break
        elif A[mid] > c:
            pr = mid
        else:
            pl = mid + 1

    if found:
        print(1)
    else:
        print(0)
