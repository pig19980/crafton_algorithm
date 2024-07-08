import heapq as pq
import sys

input = sys.stdin.readline


waitingPQ = []  # (e, s)
runningPQ = []  # (s, e)
check_list = set([])

N = int(input())

for _ in range(N):
    s, e = map(int, input().split(" "))
    if s > e:
        s, e = e, s
    pq.heappush(waitingPQ, (e, s))
    check_list.add(s)

check_list = sorted(check_list)
# print(check_list)

d = int(input())

max_cnt = -1

# print("init", cur_s, cur_e)
# print(waitingPQ)
# print(runningPQ)
# print()

for cur_s in check_list:
    if len(waitingPQ) == 0 and len(runningPQ) == 0:
        break
    cur_e = cur_s + d
    while len(waitingPQ) != 0 and waitingPQ[0][0] <= cur_e:
        e, s = pq.heappop(waitingPQ)
        if s < cur_s:
            continue
        pq.heappush(runningPQ, (s, e))

    while len(runningPQ) != 0 and runningPQ[0][0] < cur_s:
        pq.heappop(runningPQ)

    # print(cur_s, cur_e)
    # print(waitingPQ)
    # print(runningPQ)
    # print()

    cnt = len(runningPQ)
    if cnt > max_cnt:
        max_cnt = cnt

    while len(waitingPQ) != 0 and waitingPQ[0][1] <= cur_s:
        pq.heappop(waitingPQ)
    while len(runningPQ) != 0 and runningPQ[0][0] == cur_s:
        pq.heappop(runningPQ)

    # print("poped")
    # print(waitingPQ)
    # print(runningPQ)
    # print()


print(max_cnt)
