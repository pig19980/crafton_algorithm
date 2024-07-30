# 10:04 10:08
N = int(input())
nums = list(map(int, input().split(" ")))
sums = [0 for _ in range(N)]

for i in range(N):
    max_sum = nums[i]
    for j in range(i):
        if nums[j] < nums[i] and max_sum < sums[j] + nums[i]:
            max_sum = sums[j] + nums[i]
    sums[i] = max_sum

print(max(sums))
