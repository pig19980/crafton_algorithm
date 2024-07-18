# 2:05 2:36
import sys

input = sys.stdin.readline
N, E = map(int, input().split(" "))

smaller_childs = [[] for _ in range(N + 1)]
bigger_childs = [[] for _ in range(N + 1)]

smaller_nums = [None for _ in range(N + 1)]
bigger_nums = [None for _ in range(N + 1)]

half = N // 2

for _ in range(E):
    b, s = map(int, input().split(" "))
    smaller_childs[b].append(s)
    bigger_childs[s].append(b)


def get_nums(childs: list, nums: list, i):
    if nums[i] != None:
        return nums[i]
    if len(childs[i]) == 0:
        nums[i] = set()
        return nums[i]

    ret = set()
    for c in childs[i]:
        ret.add(c)
        ret.update(get_nums(childs, nums, c))
    nums[i] = ret
    return ret


not_centers = 0

for i in range(1, N + 1):
    smallers = get_nums(smaller_childs, smaller_nums, i)
    biggers = get_nums(bigger_childs, bigger_nums, i)
    if len(smallers) > half or len(biggers) > half:
        not_centers += 1

print(not_centers)
