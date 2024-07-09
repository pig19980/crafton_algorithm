import sys

input = sys.stdin.readline

N, C = map(int, input().split(" "))
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()
indexs = list(range(C - 1))
indexs.append(len(houses) - 1)


def print_cur_choice():
    ret = []
    for i in indexs:
        ret.append(houses[i])
    print(ret)


if C == 2:
    print(houses[len(houses) - 1] - houses[0])
    exit()


# Max_min = 9000000000
# for i in range(C - 1):
#     if (houses[indexs[i + 1]] - houses[indexs[i]]) < Max_min:
#         Max_min = houses[indexs[i + 1]] - houses[indexs[i]]

# print(houses)
# print_cur_choice()

step = 0

while True:
    # print_cur_choice()
    changed = False
    for i in range(1, C - 1):
        cur_gap = min(
            houses[indexs[i]] - houses[indexs[i - 1]],
            houses[indexs[i + 1]] - houses[indexs[i]],
        )
        left_gap = min(
            houses[indexs[i] - 1] - houses[indexs[i - 1]],
            houses[indexs[i + 1]] - houses[indexs[i] - 1],
        )
        right_gap = min(
            houses[indexs[i] + 1] - houses[indexs[i - 1]],
            houses[indexs[i + 1]] - houses[indexs[i] + 1],
        )
        if cur_gap >= left_gap and cur_gap >= right_gap:
            continue
        changed = True

        # find good point of i
        l, r = indexs[i - 1] + 1, indexs[i + 1] - 1
        while True:
            # check i is local max
            mid = (l + r) // 2
            # print(l, r)
            # print_cur_choice()
            cur_gap = min(
                houses[mid] - houses[indexs[i - 1]],
                houses[indexs[i + 1]] - houses[mid],
            )
            left_gap = min(
                houses[mid - 1] - houses[indexs[i - 1]],
                houses[indexs[i + 1]] - houses[mid - 1],
            )
            right_gap = min(
                houses[mid + 1] - houses[indexs[i - 1]],
                houses[indexs[i + 1]] - houses[mid + 1],
            )

            if cur_gap >= left_gap and cur_gap >= right_gap:
                indexs[i] = mid
                break

            # check bound and change
            if left_gap > cur_gap:
                changed = True
                r = mid - 1
            else:
                changed = True
                l = mid + 1

        break

    if not changed:
        break

    step += 1
    # print_cur_choice()
    # check cur cost and check changed
    if not changed:
        break
    # cur_min = 9000000000
    # for i in range(C - 1):
    #     if houses[indexs[i + 1]] - houses[indexs[i]] < cur_min:
    #         cur_min = houses[indexs[i + 1]] - houses[indexs[i]]
    # print(cur_min)
    # if cur_min == Max_min:
    #     break
    # Max_min = cur_min


# print_cur_choice()
Max_min = 9000000000
for i in range(C - 1):
    if (houses[indexs[i + 1]] - houses[indexs[i]]) < Max_min:
        Max_min = houses[indexs[i + 1]] - houses[indexs[i]]
print(Max_min)
