# PROJECT EULER PROBLEM 066
import time
from math import isqrt
from project_euler import is_square


start = time.time()
n = 90
maxd = 5
maxx = 9
for d in range(9, n):
    if is_square(d):
        continue
    else:
        x = isqrt(d + 1)
        active = True
        while active:
            if isqrt((x**2 - 1) // d)**2 * d == x**2 - 1:
                active = False
                if x > maxx:
                    maxd = d
                    maxx = x
            else:
                x += 1
                while x**2 % d != 1:
                    x += 1

print(maxx, maxd)

end = time.time()
print(f"Program runtime: {end - start} seconds")
