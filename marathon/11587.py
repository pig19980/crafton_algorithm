# 10:21 10:53
import sys

input = sys.stdin.readline

keyboard = {
    1: [],
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}


N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())
check = list(map(int, input().rstrip()))

cnt = 0
for word in words:
    if len(word) != len(check):
        continue
    found = True
    for idx in range(len(check)):
        if word[idx] not in keyboard[check[idx]]:
            found = False
            break
    if found:
        cnt += 1

print(cnt)
