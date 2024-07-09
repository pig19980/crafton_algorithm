A, B = input().split(" ")
A = list(A)
B = list(B)
A[0], A[-1] = A[-1], A[0]
B[0], B[-1] = B[-1], B[0]
A = int("".join(A))
B = int("".join(B))
if A > B:
    print(A)
else:
    print(B)
