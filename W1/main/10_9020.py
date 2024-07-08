T = int(input())

primes = [2]

for n in range(3, 10000):
    is_prime = True
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(n)

# print(primes)

for _ in range(T):
    got = int(input())
    min_gap = 10000
    small = got // 2
    big = got - small
    found = False
    while found == False:
        if small in primes and big in primes:
            break
        small -= 1
        big += 1

    print(small, big)
