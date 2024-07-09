S = int(input())
S *= int(input())
S *= int(input())
S = str(S)
for i in range(10):
    print(S.count(str(i)))
