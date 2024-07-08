import heapq

import sys

input = sys.stdin.readline

smallMaxHeap = []
bigMinHeap = []

N = int(input())
for _ in range(N):
    got = int(input())
    if len(smallMaxHeap) == len(bigMinHeap):
        if len(smallMaxHeap) == 0:
            heapq.heappush(smallMaxHeap, -got)
        else:
            sval = -heapq.heappop(smallMaxHeap)
            bval = heapq.heappop(bigMinHeap)
            vals = sorted([got, sval, bval])

            heapq.heappush(smallMaxHeap, -vals[0])
            heapq.heappush(smallMaxHeap, -vals[1])

            heapq.heappush(bigMinHeap, vals[2])
    else:
        if len(bigMinHeap) == 0:
            sval = -heapq.heappop(smallMaxHeap)
            vals = sorted([got, sval])
            heapq.heappush(smallMaxHeap, -vals[0])
            heapq.heappush(bigMinHeap, vals[1])
        else:
            sval = -heapq.heappop(smallMaxHeap)
            bval = heapq.heappop(bigMinHeap)
            vals = sorted([got, sval, bval])

            heapq.heappush(smallMaxHeap, -vals[0])

            heapq.heappush(bigMinHeap, vals[1])
            heapq.heappush(bigMinHeap, vals[2])

    # print(got, smallMaxHeap, bigMinHeap)
    print(-smallMaxHeap[0])
