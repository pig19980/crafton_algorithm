# 10:01 10:17
import sys
import heapq

input = sys.stdin.readline

N, K, S = map(int, input().split(" "))
left_house = []
right_house = []

for _ in range(N):
    loc, num = map(int, input().split(" "))
    dist = loc - S
    if dist == 0:
        continue
    elif dist > 0:
        heapq.heappush(left_house, (-dist, num))
    else:
        heapq.heappush(right_house, (dist, num))


tot_dist = 0
while left_house:
    cur_num = 0
    tot_dist += -left_house[0][0] * 2
    while left_house and cur_num < K:
        dist, num = heapq.heappop(left_house)
        if cur_num + num <= K:
            cur_num += num
        else:
            heapq.heappush(left_house, (dist, cur_num + num - K))
            cur_num = K

while right_house:
    cur_num = 0
    tot_dist += -right_house[0][0] * 2
    while right_house and cur_num < K:
        dist, num = heapq.heappop(right_house)
        if cur_num + num <= K:
            cur_num += num
        else:
            heapq.heappush(right_house, (dist, cur_num + num - K))
            cur_num = K

print(tot_dist)
