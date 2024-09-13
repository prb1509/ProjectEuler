def count_collatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

n = 1
max_count = 0
max_n = 0
while n < 1000000:
    n += 1
    current_count = count_collatz(n)
    if current_count > max_count:
        max_n = n 
        max_count = current_count
    # max_count = max(max_count,count_collatz(n))
    # print(max_count)
print(max_n)