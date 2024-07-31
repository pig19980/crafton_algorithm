# 10:06
from collections import defaultdict

N, K = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

beforedic = defaultdict(int)
maxlen = 0
curlen = 0

lidx, ridx = 0, 0

while lidx != N or ridx != N:
    overnum = -1
    while ridx < N:
        beforedic[nums[ridx]] += 1
        curlen += 1
        if beforedic[nums[ridx]] > K:
            overnum = nums[ridx]
            ridx += 1
            break
        if curlen > maxlen:
            maxlen = curlen
        ridx += 1
    while lidx < ridx:
        beforedic[nums[lidx]] -= 1
        if beforedic[nums[lidx]] == 0:
            beforedic.pop(nums[lidx])
        if nums[lidx] == overnum:
            curlen -= 1
            lidx += 1
            break
        curlen -= 1
        lidx += 1


print(maxlen)
