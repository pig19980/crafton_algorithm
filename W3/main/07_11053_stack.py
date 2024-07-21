import bisect

N = int(input())
nums = list(map(int, input().split(" ")))

stack = [-1]
cnt = 0

for num in nums:
    bn = stack[-1]
    if bn < num:
        stack.append(num)
        cnt += 1
    else:
        idx = bisect.bisect_left(stack, num)
        stack[idx] = num

print(cnt)
