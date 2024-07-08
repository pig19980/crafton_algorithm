import heapq as pq
import sys

input = sys.stdin.readline


class stagedElem:
    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __lt__(self, other):
        if self.e == other.e:
            return self.s < other.s
        return self.e < other.e

    def __repr__(self):
        return f"({self.s}, {self.e})"


class runningElem:
    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __lt__(self, other):
        if self.s == other.s:
            return self.e > other.e
        return self.s < other.s

    def __repr__(self):
        return f"({self.s}, {self.e})"


waitingPQ = []
stagedPQ: list[stagedElem] = []
runningPQ: list[runningElem] = []


N = int(input())

for _ in range(N):
    s, e = map(int, input().split(" "))
    if s > e:
        s, e = e, s
    pq.heappush(waitingPQ, (s, e))
d = int(input())


cur_s = waitingPQ[0][0]
cur_e = cur_s + d

max_cnt = -1


# print("init")
# print(waitingPQ)
# print(stagedPQ)
# print(runningPQ)
# print()

while len(waitingPQ) != 0 or len(stagedPQ) != 0 or len(runningPQ) != 0:
    while len(waitingPQ) != 0 and waitingPQ[0][0] <= cur_e:
        s, e = pq.heappop(waitingPQ)
        if s < cur_s:
            continue
        pq.heappush(stagedPQ, stagedElem(s, e))

    while len(stagedPQ) != 0 and stagedPQ[0].e <= cur_e:
        telem = pq.heappop(stagedPQ)
        pq.heappush(runningPQ, runningElem(telem.s, telem.e))

    while len(runningPQ) != 0 and runningPQ[0].s < cur_s:
        pq.heappop(runningPQ)

    # print(cur_s, cur_e)
    # print(waitingPQ)
    # print(stagedPQ)
    # print(runningPQ)
    # print()

    cnt = len(runningPQ)
    if cnt > max_cnt:
        max_cnt = cnt

    while len(waitingPQ) != 0 and waitingPQ[0][0] <= cur_s:
        pq.heappop(waitingPQ)
    while len(stagedPQ) != 0 and stagedPQ[0].s <= cur_s:
        pq.heappop(stagedPQ)
    while len(runningPQ) != 0 and runningPQ[0].s == cur_s:
        pq.heappop(runningPQ)

    # print("poped")
    # print(stagedPQ)
    # print(runningPQ)
    # print()

    cur_s = 9876543210
    if len(waitingPQ) != 0 and waitingPQ[0][0] < cur_s:
        cur_s = waitingPQ[0][0]
    if len(stagedPQ) != 0 and stagedPQ[0].s < cur_s:
        cur_s = stagedPQ[0].s
    if len(runningPQ) != 0 and runningPQ[0].s < cur_s:
        cur_s = runningPQ[0].s

    cur_e = cur_s + d


print(max_cnt)
