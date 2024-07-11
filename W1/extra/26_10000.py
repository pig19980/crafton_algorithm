# 8:50 ~ 9:50
# 9:29 ~ 11:00
import sys, math

input = sys.stdin.readline
circles_lr = []

LEFT = 1
RIGHT = -1

N = int(input())
for _ in range(N):
    x, r = map(int, input().split())
    circles_lr.append((x - r, x + r))

print(circles_lr)
circles_lr.sort(key=lambda x: (x[0], -x[1]))

print(circles_lr)

circle_points = []
for i, (l, r) in enumerate(circles_lr):
    circle_points.append((l, LEFT, i))
    circle_points.append((r, RIGHT, -i))

circle_points.append((-math.inf, LEFT, -1))
circle_points.append((math.inf, RIGHT, -1))

circle_points.sort()
print(circle_points)


def get_elem(elem):
    return (elem[0], elem[1] * elem[2], dir)


stack = [(-1, -1, True)]

cur_upper = -1
before_loc = -math.inf
cutted = True

cnt = 0


for i in range(1, len(circle_points)):
    cur_x, cur_name, cur_dir = get_elem(circle_points[i])
    before_name, before_upper, before_cutted = stack[-1]

    print(cur_x, before_loc, cur_name, cur_upper, cutted)
    # 같으면 before_loc update 하고 cnt += 1
    # cutted가 되지 않았다면 cnt += 1
    if cur_name == before_name:
        stack.pop()
        cnt += 1
        # cut 되지 않고 접하는 것으로 원이 닫힌 경우
        if not cutted and before_loc is cur_x:
            cnt += 1
        before_loc = cur_x
        cur_upper = before_upper
        cutted = before_cutted
    else:
        if cur_x == before_loc:
            cutted = False
        before_loc = cur_x
        cur_upper = cur_name

        stack.append((cur_name, before_name, cutted))
    print(stack, cnt)

print(cnt)
