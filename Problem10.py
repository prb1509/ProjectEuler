primes = [2]
n = 2000000
for i in range(3,n):
    is_prime = True
    for prime in primes:
        if prime > i**0.5:
            break
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print(sum(primes))