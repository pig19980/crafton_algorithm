# 각 사대마다 몇 마리씩 잡을 수 있는지 구하는 코드

import sys

INF = 100000000000
input = sys.stdin.readline

M, N, L = map(int, input().split(" "))
mans = list(map(int, input().split(" ")))

upper_dig = []
lower_dig = []
for _ in range(N):
    x, y = map(int, input().split(" "))
    # animals.append((x, y))
    lower_dig.append(-x + y)
    upper_dig.append(x + y)


upper_dig.sort()
lower_dig.sort()

lower_dig.append(INF)
upper_dig.append(INF)

print(lower_dig)
print(upper_dig)

max_cnt = -1
for man in mans:
    lower_bound = man - L
    upper_bound = man + L
    print(lower_bound, upper_bound)

    left_idx, right_idx = 0, 0
    lp, rp = 0, N
    while True:
        cp = (lp + rp - 1) // 2 + 1
        # print(lp, rp, cp, lower_dig[cp])
        if lower_bound < lower_dig[cp]:
            rp = cp - 1
        elif lower_bound == lower_dig[cp]:
            lp = cp
        else:
            lp = cp + 1
        if lp >= rp:
            break

    left_idx = rp

    # print("l idx", left_idx)
    lp, rp = 0, N
    while True:
        cp = (lp + rp - 1) // 2 + 1
        # print(lp, rp, cp)
        # print(lower_dig[cp])
        if upper_bound < upper_dig[cp]:
            rp = cp - 1
        elif upper_bound == upper_dig[cp]:
            lp = cp
        else:
            lp = cp + 1
        if lp >= rp:
            break

    right_idx = rp

    print("result", left_idx, right_idx)
    cnt = left_idx - right_idx + 1
    print(cnt)
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
