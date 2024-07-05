primes = [2]

for n in range(3, 1000):
    is_prime = True
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(n)


N = input()
nums = list(map(int, input().split(" ")))

ret = 0
for num in nums:
    if num in primes:
        ret += 1

print(ret)
