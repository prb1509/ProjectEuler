import timeit
def problem3():
    prime_divisors = []
    n = 600851475143
    while n > 1:
        sqrt_n  = int(n**0.5) 
        for i in range(2,sqrt_n):
            if n % i == 0:
                    prime_divisors.append(i)
                    n //= i
                    break
            if i == sqrt_n - 1:
                prime_divisors.append(n)
                n = 1 
    # print(max(prime_divisors))
print(timeit.timeit(problem3,number=100))