import bisect, sys
from collections import deque

N = int(input())
nums = list(map(int, input().split(" ")))
befores = [None for _ in range(N)]


def get_num(idx):
    if idx == -1:
        return -2000000000
    return nums[idx]


stack = [-1]
cnt = 0

for idx in range(N):
    bidx = stack[-1]
    if get_num(bidx) < nums[idx]:
        stack.append(idx)
        befores[idx] = bidx
        cnt += 1
    else:
        cidx = bisect.bisect_left(stack, nums[idx], key=get_num)
        stack[cidx] = idx
        befores[idx] = stack[cidx - 1]

print(cnt)
print_stack = []
cur = stack[-1]
while cur >= 0:
    print_stack.append(nums[cur])
    cur = befores[cur]

for n in print_stack[::-1]:
    print(f"{n} ", end="")
print()
