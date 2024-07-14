import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split(" "))
Num = input()
smaller_than_right = deque()
Ns = [[-1, -1, 1]]

for i in range(N):
    n = int(Num[i])
    # (val, before_idx, next_idx)
    Ns.append([n, i, i + 2])
    if i != N - 1:
        m = int(Num[i + 1])
        if n < m:
            smaller_than_right.append(i + 1)

Ns.append([-1, N, N + 2])


for _ in range(K):
    if len(smaller_than_right) > 0:
        del_idx = smaller_than_right.popleft()
        before_idx = Ns[del_idx][1]
        next_idx = Ns[del_idx][2]

        Ns[before_idx][2] = next_idx
        Ns[next_idx][1] = before_idx

        if Ns[before_idx][0] != -1 and Ns[before_idx][0] < Ns[next_idx][0]:
            smaller_than_right.appendleft(before_idx)
    else:
        del_idx = Ns[N + 1][1]
        before_idx = Ns[del_idx][1]
        next_idx = Ns[del_idx][2]

        Ns[before_idx][2] = next_idx
        Ns[next_idx][1] = before_idx


idx = Ns[0][2]
while idx != N + 1:
    print(Ns[idx][0], end="")
    idx = Ns[idx][2]
print()
