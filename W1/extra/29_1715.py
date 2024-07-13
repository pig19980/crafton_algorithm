# 12:39 12:55
import sys, heapq

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

pq = []

for elem in arr:
    heapq.heappush(pq, elem)


sum = 0
while len(pq) >= 2:
    left = heapq.heappop(pq)
    right = heapq.heappop(pq)
    part = left + right

    sum += part
    heapq.heappush(pq, part)

print(sum)
