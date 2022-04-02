# PROJECT EULER PROBLEM 34
import time
from math import factorial


start = time.time()

maximum = factorial(9)
print(factorial(9))

for d in range(1, 10):
    if 10**d > maximum*(d+1):
        print(d)

special = []
factorial_list = [factorial(k) for k in range(0, 10)]
print(factorial_list)
for n in range(3, 7*factorial_list[9]):
    string = str(n)
    s = 0
    for d in string:
        digit = int(d)
        s += factorial_list[digit]
    if s == n:
        special.append(n)

print(sum(special))
end = time.time()
print(f"Program runtime: {end - start} seconds")
