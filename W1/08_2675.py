T = int(input())
for test_case in range(T):
    repeat, string = input().split(" ")
    repeat = int(repeat)
    ret = ""
    for c in string:
        ret += c * repeat
    print(ret)
