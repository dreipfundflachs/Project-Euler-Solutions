# PROJECT EULER - PROBLEM 30
import time


start = time.time()
# Obtaining an upper bound for the number of digits (7)
m = 7*9**5
print(m)

special = []
for n in range(2, 10**6):
    string = str(n)
    s = 0
    for digit in string:
        s += int(digit)**5
    if s == n:
        special.append(n)
print(special)
print(sum(special))


end = time.time()
print(f"Program runtime: {end - start} seconds")
