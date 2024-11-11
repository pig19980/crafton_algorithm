# 1h
import sys


def loc_idx(j, i):
    return (j % N) * N + i % N


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def are_coprime(a, b):
    return gcd(a, b) == 1


input = sys.stdin.readline

N = int(input())
init_map = []
ret_map = [[None for _ in range(N**2)] for _ in range(N**2)]

for _ in range(N**2):
    init_map.append(list(map(int, input().split(" "))))


# if x in (j, i)
row_product = [1 for _ in range(N**2)]  # idx = j
col_product = [1 for _ in range(N**2)]  # idx = i
loc_product = [1 for _ in range(N**2)]  # idx = (j % N) * N + i % N


for j in range(N**2):
    for i in range(N**2):
        if init_map[j][i] == 0:
            continue
        ret_map[j][i] = init_map[j][i]

        row_product[j] *= init_map[j][i]
        col_product[i] *= init_map[j][i]
        loc_product[loc_idx(j, i)] *= init_map[j][i]

for j in range(N**2):
    for i in range(N**2):
        if ret_map[j][i] != None:
            continue
        checking_product = 1
        checking_product *= row_product[j]
        checking_product *= col_product[i]
        checking_product *= loc_product[loc_idx(j, i)]

        for num in range(2, 1000001):
            if are_coprime(num, checking_product):
                ret_map[j][i] = num
                row_product[j] *= num
                col_product[i] *= num
                loc_product[loc_idx(j, i)] *= num
                break


for j in range(N**2):
    for i in range(N**2):
        print(ret_map[j][i], end=" ")
    print()
