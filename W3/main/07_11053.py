# 10:35 11:10
import math

N = int(input())
nums = list(map(int, input().split(" ")))

costs = [[math.inf for _ in range(len(nums) + 1)] for _ in range(N + 1)]
for i in range(len(nums) + 1):
    costs[0][i] = 0


for length in range(1, N + 1):
    for idx in range(length - 1, len(nums)):
        if costs[length - 1][idx - 1] < nums[idx]:
            if nums[idx] < costs[length][idx - 1]:
                costs[length][idx] = nums[idx]
            else:
                costs[length][idx] = costs[length][idx - 1]
        else:
            costs[length][idx] = costs[length][idx - 1]


max_len = N
while max_len > 0:
    if costs[max_len][N - 1] != math.inf:
        break
    max_len -= 1
print(max_len)
