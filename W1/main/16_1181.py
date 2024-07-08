from functools import cmp_to_key


def cmp_string(s1, s2):
    if len(s1) == len(s2):
        l = len(s1)
        for i in range(l):
            if s1[i] != s2[i]:
                return ord(s1[i]) - ord(s2[i])
        return 0
    else:
        return len(s1) - len(s2)


N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

arr.sort(key=cmp_to_key(cmp_string))
prev = ""
for s in arr:
    if s == prev:
        continue
    print(s)
    prev = s
