# 12:31 12:38
from collections import deque

N = int(input())
dq = deque()

for i in range(1, N + 1):
    dq.append(i)

while len(dq) > 1:
    # print(dq)
    dq.popleft()
    left = dq.popleft()
    dq.append(left)

print(dq.pop())
