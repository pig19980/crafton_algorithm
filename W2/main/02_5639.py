# 4 : 06

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break


def print_huwe(s, e):
    # print(s, e)
    if s + 1 == e:
        print(arr[s])
        return
    if s >= e:
        return

    i = s + 1
    while i < e and arr[i] < arr[s]:
        i += 1
    # print(i)
    print_huwe(s + 1, i)
    print_huwe(i, e)
    print(arr[s])


print_huwe(0, len(arr))
