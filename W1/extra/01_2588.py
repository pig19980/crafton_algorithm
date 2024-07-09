A = input()
B = input()
Anum = int(A)
Bnum = int(B)

for c in B[::-1]:
    print(Anum * int(c))
print(Anum * Bnum)
