# 9:59
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
unions = list(range(N + 1))


def get_top(pos):
    if unions[pos] == pos:
        return pos
    return get_top(unions[pos])


for _ in range(M):
    s, e = map(int, input().split(" "))
    s_top, e_top = get_top(s), get_top(e)
    if s < e:
        unions[e_top] = s_top
    else:
        unions[s_top] = e_top

cnt = 0
founds = set()

for idx in range(1, N + 1):
    if unions[idx] == idx:
        cnt += 1

print(cnt)
