m = 0
for i in range(100,999):
    for j in range(i,999):
        if i % 11 != 0 and j % 11 != 0:
            continue
        n = i * j
        if str(n) == str(n)[::-1]:
            m = max(m,n)
print(m)