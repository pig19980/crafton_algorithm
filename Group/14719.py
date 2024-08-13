# 10:00
W, H = map(int, input().split(" "))
heights = [0] + list(map(int, input().split(" ")))

sum_H = 0
stack = []

top_idx = 0
while top_idx < len(heights) - 1:
    if heights[top_idx + 1] < heights[top_idx]:
        break
    else:
        top_idx += 1

stack.append((top_idx, heights[top_idx]))

while top_idx < len(heights):
    idx = top_idx + 1
    while idx < len(heights):
        before_idx, before_h = stack[-1]
        if before_h < heights[idx]:
            break
        elif before_h > heights[idx]:
            stack.append((idx, heights[idx]))
        else:
            stack.pop()
            stack.append((idx, heights[idx]))
        idx += 1

    if idx == len(heights):
        break

    before_idx, before_h = stack.pop()
    while stack:
        left_idx, left_h = stack[-1]
        if left_h < heights[idx]:
            sum_H += (left_h - before_h) * (idx - left_idx - 1)
            before_idx, before_h = stack.pop()
        else:
            sum_H += (heights[idx] - before_h) * (idx - left_idx - 1)
            break
    if left_h == heights[idx]:
        stack.pop()
    stack.append((idx, heights[idx]))
    top_idx = idx

print(sum_H)
