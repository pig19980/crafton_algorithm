# 10:25
N = int(input())
if N % 2:
    print(("CY"))
else:
    print("SK")

# wins = [None] * 1001


# def get_win(n):
#     if wins[n]:
#         return wins[n]
#     if n == 1:
#         wins[1] = 0
#         return 0
#     if get_win(n - 1) == 0:
#         wins[n] = 1
#         return 1
#     if n - 3 >= 1 and get_win(n - 3) == 0:
#         wins[n] = 1
#         return 1
#     wins[n] = 0
#     return 0


# get_win(20)
# print(wins[:21])
