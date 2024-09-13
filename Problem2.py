#Even fibonacci numbers are f_3, f_6, f_9 ... 
n = 3
s = 0
gt_4mil = False
phi = (1 + 5**0.5) / 2
psi = (1 - 5**0.5) / 2
while not gt_4mil:
    f = (phi**n - psi**n) / (phi - psi)
    s += int(f) #rounding errors are insignificant
    n += 3
    f = (phi**n - psi**n) / (phi - psi)
    gt_4mil = f > 4000000
print(s)