# 8:50 ~ 9:50
# 9:29 ~ 11:00
import sys, math

input = sys.stdin.readline

LEFT = 1
RIGHT = -1

N = int(input())
circle_points = []
for _ in range(N):
    x, r = map(int, input().split())
    l, r = x - r, x + r
    circle_points.append((l, LEFT))
    circle_points.append((r, RIGHT))

circle_points.append((-math.inf, LEFT))
circle_points.append((math.inf, RIGHT))


# 좌표가 작고 circle이 닫히는 RIGHT 부분일 수록 앞으로
circle_points.sort()

# 위의 circle이 잘렸는지 아닌지 저장하는 stack
# 처음은 inf만큼 큰 원이 있다고 생각하며, 잘려 있음
stack = [True]

before_loc = -math.inf
cnt = 0


for i in range(1, len(circle_points)):
    cur_loc, cur_dir = circle_points[i]
    cutted = stack[-1]

    if cur_dir == RIGHT:
        # pop stack
        stack.pop()
        cnt += 1
        if cutted and before_loc == cur_loc:
            cnt += 1
        before_loc = cur_loc
    else:
        # if gap is existed between cur loc and befor loc
        # upper circle is cutted
        if cur_loc != before_loc:
            stack[-1] = True

        before_loc = cur_loc

        # first set this circle is not cutted
        stack.append(False)


print(cnt)
