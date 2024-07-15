# 10:12
from copy import deepcopy

MAX = 9876543210
MIN = -9876543210

N = int(input())
Nums = list(map(int, input().split(" ")))
ops = list(map(int, input().split(" ")))

max_arr = [MIN for _ in range(ops[3] + 1)]
max_arr = [deepcopy(max_arr) for _ in range(ops[2] + 1)]
max_arr = [deepcopy(max_arr) for _ in range(ops[1] + 1)]
max_arr = [deepcopy(max_arr) for _ in range(ops[0] + 1)]

max_arr = [deepcopy(max_arr) for _ in range(N + 1)]

min_arr = [MAX for _ in range(ops[3] + 1)]
min_arr = [deepcopy(min_arr) for _ in range(ops[2] + 1)]
min_arr = [deepcopy(min_arr) for _ in range(ops[1] + 1)]
min_arr = [deepcopy(min_arr) for _ in range(ops[0] + 1)]

min_arr = [deepcopy(min_arr) for _ in range(N + 1)]


def div(a: int, b: int):
    if a > 0:
        return a // b
    else:
        return -((-a) // b)


operator = [int.__add__, int.__sub__, int.__mul__, div]


def get_min(len, ops: list):
    for i in range(4):
        if ops[i] < 0:
            return MAX

    if min_arr[len][ops[0]][ops[1]][ops[2]][ops[3]] != MAX:
        return min_arr[len][ops[0]][ops[1]][ops[2]][ops[3]]

    if len == 2:
        for i in range(4):
            if ops[i] == 1:
                break
        ret = operator[i](Nums[0], Nums[1])
        # print("bound condition")
        # print(ops)
        # print(i, ret)
        # print("=======")
        min_arr[len][ops[0]][ops[1]][ops[2]][ops[3]] = ret
        return ret

    ret = MAX
    for i in range(4):
        ops[i] -= 1
        temp_ret = get_min(len - 1, ops)
        if temp_ret != MAX:
            # print("check child and calculate")
            # print(i, temp_ret, Nums[len - 1], ops)
            temp_ret = operator[i](temp_ret, Nums[len - 1])
            # print(temp_ret)
            # print("=========")
            ret = min(ret, temp_ret)
        ops[i] += 1

    min_arr[len][ops[0]][ops[1]][ops[2]][ops[3]] = ret
    return ret


def get_max(len, ops: list):
    for i in range(4):
        if ops[i] < 0:
            return MIN

    if max_arr[len][ops[0]][ops[1]][ops[2]][ops[3]] != MIN:
        return max_arr[len][ops[0]][ops[1]][ops[2]][ops[3]]

    if len == 2:
        for i in range(4):
            if ops[i] == 1:
                break
        ret = operator[i](Nums[0], Nums[1])
        # print("bound condition")
        # print(ops)
        # print(i, ret)
        # print("=======")
        max_arr[len][ops[0]][ops[1]][ops[2]][ops[3]] = ret
        return ret

    ret = MIN
    for i in range(4):
        ops[i] -= 1
        temp_ret = get_max(len - 1, ops)
        if temp_ret != MIN:
            # print("check child and calculate")
            # print(i, temp_ret, Nums[len - 1], ops)
            temp_ret = operator[i](temp_ret, Nums[len - 1])
            # print(temp_ret)
            # print("=========")
            ret = max(ret, temp_ret)
        ops[i] += 1

    max_arr[len][ops[0]][ops[1]][ops[2]][ops[3]] = ret
    return ret


print(get_max(N, ops))
print(get_min(N, ops))
