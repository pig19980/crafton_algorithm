import sys
from heapq import heappush, heappop

input = sys.stdin.readline

M, N, L = map(int, input().split(" "))
mans = list(map(int, input().split(" ")))

waitpq = []
checkpq = []
cannot = 0

for _ in range(N):
    x, y = map(int, input().split(" "))
    heappush(waitpq, (x + y, x, y))

mans.sort()


for man in mans:
    right_bound = man + L
    left_bound = -man + L
    while checkpq:
        checkkey = checkpq[0]
        if checkkey > left_bound:
            heappop(checkpq)
            cannot += 1
        else:
            break

    while waitpq:
        waitkey, x, y = waitpq[0]
        if waitkey <= right_bound:
            heappop(waitpq)
            heappush(checkpq, -x + y)
        else:
            break

    while checkpq:
        checkkey = checkpq[0]
        if checkkey <= left_bound:
            heappop(checkpq)
        else:
            break


cannot += len(checkpq) + len(waitpq)
print(N - cannot)
