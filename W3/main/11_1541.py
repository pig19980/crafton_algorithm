# 11:56 12:16
got = input()


min_num = 0
num = []
for i in range(len(got)):
    if got[i] not in ["-", "+"]:
        num.append(got[i])
    elif got[i] == "+":
        min_num += int("".join(num))
        num = []
    else:
        min_num += int("".join(num))
        num = []
        break
    if i == len(got) - 1:
        min_num += int("".join(num))


if i == len(got) - 1:
    print(min_num)
    exit()

minus_num = 0
for j in range(i + 1, len(got)):
    if got[j] not in ["-", "+"]:
        num.append(got[j])
    elif got[j] == "+":
        minus_num += int("".join(num))
        num = []
    elif got[j] == "-":
        minus_num += int("".join(num))
        num = []
        min_num -= minus_num
        minus_num = 0
    if j == len(got) - 1:
        minus_num += int("".join(num))
        num = []
        min_num -= minus_num
        minus_num = 0


print(min_num)
