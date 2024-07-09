N, r, c = map(int, input().split(" "))
# print(4 >> 2)

mult = [[0, 1], [2, 3]]


def get_part(min, r, c, l):
    # print(min, r, c, l)
    if l == 1:
        return min + mult[r][c]
    block = 1 << (2 * l - 2)
    div = 1 << (l - 1)

    # print(block, div, mult[r // div][c // div])

    next_min = min + block * mult[r // div][c // div]
    next_r = r if r < div else r - div
    next_c = c if c < div else c - div
    return get_part(next_min, next_r, next_c, l - 1)


print(get_part(0, r, c, N))
