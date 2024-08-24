# 10:09 10:14
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
not_heard = set()
names = set()

for _ in range(N):
    not_heard.add(input().rstrip())
for _ in range(M):
    got = input().rstrip()
    if got in not_heard:
        names.add(got)

names = sorted(list(names))
print(len(names))
for name in names:
    print(name)
