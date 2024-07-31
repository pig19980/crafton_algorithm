# 10:00 10:05
import sys

input = sys.stdin.readline

N = int(input())
incompany = set()
for _ in range(N):
    name, cmd = input().rstrip().split(" ")
    if cmd == "enter":
        incompany.add(name)
    else:
        incompany.remove(name)
incompany = sorted(list(incompany))

for name in reversed(incompany):
    print(name)
