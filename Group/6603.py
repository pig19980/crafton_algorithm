# 10:09 10:19
import sys

input = sys.stdin.readline


def print_visited(nums, visited, min_idx, level):
    if level == 6:
        output = ""
        for i in range(len(nums)):
            if visited[i]:
                output += str(nums[i]) + " "
        print(output)
        return
    for nidx in range(min_idx, len(nums)):
        visited[nidx] = True
        print_visited(nums, visited, nidx + 1, level + 1)
        visited[nidx] = False


while True:
    got = list(map(int, input().split(" ")))
    if len(got) == 1:
        break
    N = got[0]
    nums = got[1:]
    visited = [False for _ in range(N)]
    print_visited(nums, visited, 0, 0)
    print()
