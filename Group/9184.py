# 10:38
import sys

input = sys.stdin.readline

W = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if 0 < a <= 20 and 0 < b <= 20 and 0 < c <= 20 and W[a][b][c]:
        return W[a][b][c]

    if a < b and b < c:
        ret = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        W[a][b][c] = ret
        return ret

    ret = (
        w(a - 1, b, c)
        + w(a - 1, b - 1, c)
        + w(a - 1, b, c - 1)
        - w(a - 1, b - 1, c - 1)
    )
    W[a][b][c] = ret
    return ret


while True:
    a, b, c = map(int, input().split(" "))
    if (a, b, c) == (-1, -1, -1):
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
