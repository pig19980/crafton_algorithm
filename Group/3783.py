import sys, math
from decimal import *

input = sys.stdin.readline

Factor_10 = 10**10

getcontext().prec = 200
getcontext().rounding = ROUND_UP

min_val = Decimal("0.0000000001")


def ceiling_deci(num: Decimal):
    return Decimal((num * Factor_10).__ceil__()) / Factor_10


def get_tripe_root(num: Decimal):
    if num == Decimal(1):
        return num
    l, r = Decimal(0), num
    while True:
        mid = ceiling_deci((l + r) / 2)
        if mid**3 == num:
            l = mid
            break
        elif mid**3 < num:
            l = mid
        else:
            r = mid - min_val
        if r - l < min_val:
            break
    return l


N = int(input())
for _ in range(N):
    num = int(input())
    ret = get_tripe_root(Decimal(num))
    print(f"{ret:.10f}")
