# 10:17 10:57


def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    num = numerator // denominator
    cur_decimal = numerator % denominator

    if cur_decimal == 0:
        return str(num)

    decimal = ""
    num = str(num)
    while True:
        cur_char = cur_decimal * 10 // denominator
        next_decimal = cur_decimal * 10 % denominator
        if next_decimal == 0:
            decimal = decimal + str(cur_char)
            break
        # cur_char로 찾는 것이 아니라, next_decimal을 stack에 넣고 이를 찾는 것으로 바꿔야 함
        if (find_idx := decimal.find(str(cur_char))) != -1:
            decimal = decimal[:find_idx] + "(" + decimal[find_idx:] + ")"
            break
        decimal = decimal + str(cur_char)
        cur_decimal = next_decimal
    return num + "." + decimal


print(fractionToDecimal(1, 2))
print(fractionToDecimal(2, 1))
print(fractionToDecimal(4, 333))
print(fractionToDecimal(1, 333))
