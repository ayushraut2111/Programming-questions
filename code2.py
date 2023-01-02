from math import *

n = int(input())
v = int(sqrt(n))
count = 0

for i in range(1, v):
    for j in range(1, v):
        equa = (i**2) + 5*i*j + 3*(j**2)
        r_equa = sqrt(equa)
        if r_equa*r_equa == equa and equa < n:
            count += 1

print(count)
