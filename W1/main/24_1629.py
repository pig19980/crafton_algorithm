num, N, div = map(int, input().split())

ret = 1


def get_rest(mult):
    if mult == 1:
        return num % div
    ret = get_rest(mult // 2)
    ret = ret * ret % div
    if mult % 2 == 1:
        ret = ret * num % div
    return ret


print(get_rest(N))
