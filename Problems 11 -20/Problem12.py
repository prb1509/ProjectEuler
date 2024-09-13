def count_divisors(n):
    n_dvisors = 0
    # while n > 1:
    for i in range(1,int(n**0.5)):
        if n % i == 0:
            # n //= i
            n_dvisors += 2
    if n**0.5 == int(n**0.5):
        n_dvisors += 1
    return n_dvisors

n = 7
while True:
    triangular_number = n * (n + 1) // 2
    n_divisors = count_divisors(triangular_number)
    if n_divisors > 500:
        break
    n += 1
print(triangular_number)