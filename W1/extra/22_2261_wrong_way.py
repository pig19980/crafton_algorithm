import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
MAX = 9876543210


def sortbyX(point):
    return point[0]


def sortbyY(point):
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


def DM_with_Y(points: list, Ymin, Ymax, Xmin, Xmax):
    if len(points) <= 1:
        return MAX
    elif len(points) < 9:
        minDist = MAX
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                dist = getDist(points[i], points[j])
                if dist < minDist:
                    minDist = dist
        return minDist

    # divide with Y
    Ymid = (Ymax + Ymin) // 2
    Ysorted = sorted(points, key=sortbyY)
    YmidIdx = bisect_left(Ysorted, Ymid, key=sortbyY)

    up_points = Ysorted[:YmidIdx]
    donw_points = Ysorted[YmidIdx:]

    up_result = DM_with_X(up_points, Ymin, Ymid, Xmin, Xmax)
    down_result = DM_with_X(donw_points, Ymid, Ymax, Xmin, Xmax)

    # merge with Y
    result = min(up_result, down_result)
    if len(up_points) == 0 or len(donw_points) == 0:
        return result
    if result == 0:
        return 0

    up_points = list(map(lambda X: X + (0,), up_points))
    donw_points = list(map(lambda X: X + (1,), donw_points))
    points = sorted(up_points + donw_points, key=sortbyXwithAxis(Ymid))

    lp, rp = None, None

    for p in points:
        if p[2] == 0:
            lp = p[:2]
        else:
            rp = p[:2]

        if lp != None and rp != None:
            dist = getDist(lp, rp)
            if dist < result:
                result = dist

    return result


def DM_with_X(points: list, Ymin, Ymax, Xmin, Xmax):
    if len(points) <= 1:
        return MAX
    elif len(points) < 9:
        minDist = MAX
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                dist = getDist(points[i], points[j])
                if dist < minDist:
                    minDist = dist
        return minDist

    # divide with X
    Xmid = (Xmax + Xmin) // 2
    Xsorted = sorted(points, key=sortbyX)
    XmidIdx = bisect_left(Xsorted, Xmid, key=sortbyX)

    left_points = Xsorted[:XmidIdx]
    right_points = Xsorted[XmidIdx:]

    left_result = DM_with_Y(left_points, Ymin, Ymax, Xmin, Xmid)
    right_result = DM_with_Y(right_points, Ymin, Ymax, Xmid, Xmax)

    # merge with X
    result = min(left_result, right_result)
    if len(left_points) == 0 or len(right_points) == 0:
        return result
    if result == 0:
        return 0

    left_points = list(map(lambda X: X + (0,), left_points))
    right_points = list(map(lambda X: X + (1,), right_points))
    points = sorted(left_points + right_points, key=sortbyYwithAxis(Xmid))

    lp, rp = None, None

    for p in points:
        if p[2] == 0:
            lp = p[:2]
        else:
            rp = p[:2]

        if lp != None and rp != None:
            dist = getDist(lp, rp)
            if dist < result:
                result = dist

    return result


N = int(input())
points = []

minX, maxX = MAX, -MAX
minY, maxY = MAX, -MAX

for _ in range(N):
    x, y = map(int, input().split(" "))
    points.append((x, y))


print(DM_with_Y(points, 0, 10001, 0, 10001))
