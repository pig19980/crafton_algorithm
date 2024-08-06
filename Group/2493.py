# 10:04

N = int(input())
tops = list(map(int, input().split(" ")))

max_idxs = []
got_top = [-1 for _ in range(N)]

for idx in range(len(tops) - 1, -1, -1):
    while max_idxs and tops[max_idxs[-1]] <= tops[idx]:
        got_top[max_idxs[-1]] = idx
        max_idxs.pop()
    max_idxs.append(idx)

for elem in got_top:
    print(f"{elem + 1} ", end="")
print()
