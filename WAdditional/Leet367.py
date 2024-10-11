# 10:50 10:57
def isPerfectSquare(num):
    left = 0
    right = num
    while left < right:
        mid = (left + right) // 2
        sqr = mid**2
        if sqr == num:
            return True
        elif sqr > num:
            right = mid
        else:
            left = mid + 1

    return False


print(isPerfectSquare(16))
print()
print(isPerfectSquare(14))
