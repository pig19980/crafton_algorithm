import sys

input = sys.stdin.readline
MAX = 9876543210

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


def getLeftboundwithMode(left, right, key, m):
    global points
    # print("get left bound", points[left:right])
    # print("left, right, key, m")
    # print(left, right, key, m)
    pl = left
    pr = right - 1
    while pl <= pr:
        while get[m](points[pl]) < key and pl < right - 1:
            pl += 1
        while get[m](points[pr]) > key and pr > left:
            pr -= 1
        if pl <= pr:
            points[pl], points[pr] = points[pr], points[pl]
            pl += 1
            pr -= 1

    idx = left
    while idx < right:
        # print(get[m](points[idx]))
        if key <= get[m](points[idx]):
            break
        idx += 1

    return idx


def DM_with_mode(left, right, Ymin, Ymax, Xmin, Xmax, mode):
    global points
    # print("divide start")
    # print("l r Ymin Ymax Xmin Xmax mode")
    # print(left, right, Ymin, Ymax, Xmin, Xmax, mode)
    # print(points[left:right])
    length = right - left
    if length <= 1:
        return MAX
    elif length < 20:
        minDist = MAX
        for i in range(left, right):
            for j in range(left, right):
                if i == j:
                    continue
                dist = getDist(points[i], points[j])
                if dist < minDist:
                    minDist = dist
        return minDist

    # divide
    if mode == 0:
        mid = (Xmax + Xmin) // 2
        arg1 = (Ymin, Ymax, Xmin, mid, 1)
        arg2 = (Ymin, Ymax, mid, Xmax, 1)
    else:
        mid = (Ymax + Ymin) // 2
        arg1 = (Ymin, mid, Xmin, Xmax, 0)
        arg2 = (mid, Ymax, Xmin, Xmax, 0)

    leftbound = getLeftboundwithMode(left, right, mid, mode)

    # print("divided")
    # print(points[left:leftbound])
    # print(points[leftbound:right])

    left_result = DM_with_mode(left, leftbound, *arg1)
    right_result = DM_with_mode(leftbound, right, *arg2)

    result = min(left_result, right_result)
    if (leftbound - left) == 0 or (right - leftbound) == 0:
        return result
    if result == 0:
        return 0

    keyfunction = sortbyCoordAxis[mode](mid)

    left_points = sorted(points[left:leftbound], key=keyfunction)
    right_points = sorted(points[leftbound:right], key=keyfunction)
    points[left:leftbound] = left_points
    points[leftbound:right] = right_points

    lp, rp = left, leftbound

    while lp != leftbound and rp != right:
        dist = getDist(points[lp], points[rp])
        if dist < result:
            result = dist
        if lp == leftbound:
            rp += 1
        elif rp == right:
            lp += 1
        elif points[lp][(mode + 1) % 2] < points[rp][(mode + 1) % 2]:
            lp += 1
        else:
            rp += 1

    return result


N = int(input())
points = []

# minX, maxX = MAX, -MAX
# minY, maxY = MAX, -MAX

for _ in range(N):
    x, y = map(int, input().split(" "))
    points.append((x, y))


print(DM_with_mode(0, len(points), -30000, 30000, -30000, 30000, 0))
