# 10:54 11:02
primes = [2]
for n in range(3, 10000001):
    found = True
    for p in primes:
        if n**2 > p:
            break
        if p % n == 0:
            found = False
            break
    if found:
        primes.append(n)

got = int(input())
for p in primes:
    if got == 1:
        break
    while got % p == 0:
        print(p)
        got //= p
