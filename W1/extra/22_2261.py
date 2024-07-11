import sys, math

input = sys.stdin.readline
MAX = math.inf

points = []


def getX(point):
    return point[0]


def getY(point):
    return point[1]


def sortbyXwithAxis(Yaxis):
    def warp(point):
        return (point[0], abs(point[1] - Yaxis))

    return warp


def sortbyYwithAxis(Xaxis):
    def warp(point):
        return (point[1], abs(point[0] - Xaxis))

    return warp


def getDist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


get = [getX, getY]
sortbyCoordAxis = [sortbyYwithAxis, sortbyXwithAxis]


def DM_with_mode(left, right, minX, maxX, minY, maxY, mode):
    global points
    # print(left, right, minX, maxX, minY, maxY, mode)
    # print(points[left:right])

    length = right - left
    if length <= 1:
        return MAX
    elif length < 3:
        minDist = MAX
        for i in range(left, right):
            for j in range(left, right):
                if i == j:
                    continue
                dist = getDist(points[i], points[j])
                if dist < minDist:
                    minDist = dist
        return minDist

    if minX == maxX and minY == maxY:
        if right - left == 1:
            return MAX
        else:
            return 0
    if minX == maxX:
        # print("X samee")
        min_gap = MAX
        temp_arr = sorted(points[left:right], key=get[1])
        # print(temp_arr)

        for i in range(right - left - 1):
            cur_gap = (temp_arr[i + 1][1] - temp_arr[i][1]) ** 2
            if cur_gap < min_gap:
                min_gap = cur_gap
        # print(min_gap)
        return min_gap
    if minY == maxY:
        # print("YYY samee")
        min_gap = MAX
        temp_arr = sorted(points[left:right], key=get[0])

        for i in range(right - left - 1):
            cur_gap = (temp_arr[i + 1][0] - temp_arr[i][0]) ** 2
            if cur_gap < min_gap:
                min_gap = cur_gap
        return min_gap

    temp_arr = points[left:right]
    temp_arr.sort(key=get[mode])
    points[left:right] = temp_arr

    mid = (left + right) // 2
    # print(points)
    # print(points[mid])

    p = left
    gap = mid - left
    before = points[p][mode]
    for i in range(left + 1, right):
        if points[i][mode] != before:
            # print(i, mid)
            if abs(mid - i) < gap:
                p = i
                gap = abs(mid - i)
                before = points[i][mode]
            else:
                break

    mid = p
    # print(points[mid])
    axis = points[mid][mode]

    if mode == 0:
        if mid - left > 0:
            arg1 = (points[left][0], points[mid - 1][0], minY, maxY, 1)
        else:
            arg1 = (-MAX, MAX, minY, maxY, 1)
        if right - mid > 0:
            arg2 = (points[mid][0], points[right - 1][0], minY, maxY, 1)
        else:
            arg2 = (-MAX, MAX, minY, maxY, 1)
    else:
        if mid - left > 0:
            arg1 = (minX, maxX, points[left][1], points[mid - 1][1], 0)
        else:
            arg1 = (minX, maxX, -MAX, MAX, 1)
        if right - mid > 0:
            arg2 = (minX, maxX, points[mid][1], points[right - 1][1], 0)
        else:
            arg2 = (minX, maxX, -MAX, MAX, 1)

    left_result = DM_with_mode(left, mid, *arg1)
    right_result = DM_with_mode(mid, right, *arg2)

    result = min(left_result, right_result)
    if (mid - left) == 0 or (right - mid) == 0:
        return result
    if result == 0:
        return 0

    # minAxis = -MAX
    # maxAxis = MAX
    # for i in range(left, mid):
    #     if points[i][mode] > minAxis:
    #         minAxis = points[i][mode]
    # for i in range(mid, right):
    #     if points[i][mode] < maxAxis:
    #         maxAxis = points[i][mode]

    # axis = (maxAxis + minAxis) // 2

    keyfunction = sortbyCoordAxis[mode](axis)

    left_points = sorted(points[left:mid], key=keyfunction)
    right_points = sorted(points[mid:right], key=keyfunction)
    points[left:mid] = left_points
    points[mid:right] = right_points

    lp, rp = left, mid
    lpoint, rpoint = points[lp], points[rp]

    print("merge part")
    # 이분탐색 써서 가장 가까운 반대편 점 찾기
    print(left, right, mid, mode, axis)
    print(left_points)
    print(right_points)
    while lp != mid - 1 or rp != right - 1:
        if lpoint[(mode + 1) % 2] != points[lp][(mode + 1) % 2]:
            lpoint = points[lp]
        if rpoint[(mode + 1) % 2] != points[rp][(mode + 1) % 2]:
            rpoint = points[rp]

        print(lp, rp, mid)
        print(points[lp], points[rp])
        print(lpoint, rpoint)
        print()

        dist = getDist(lpoint, rpoint)
        if dist < result:
            result = dist

        if lp == mid - 1:
            rp += 1
        elif rp == right - 1:
            lp += 1
        elif points[lp][(mode + 1) % 2] < points[rp][(mode + 1) % 2]:
            lp += 1
        else:
            rp += 1

    # print("done merge")

    return result


N = int(input())
points = []

minX, maxX = MAX, -MAX
minY, maxY = MAX, -MAX

for _ in range(N):
    x, y = map(int, input().split(" "))

    if minX > x:
        minX = x
    if maxX < x:
        maxX = x
    if minY > y:
        minY = y
    if maxY < y:
        maxY = y

    points.append((x, y))


print(DM_with_mode(0, len(points), minX, maxX, minY, maxY, 1))
