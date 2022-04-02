# PROJECT EULER PROBLEM 048
import time


start = time.time()
s = 0
cut = 10**10
for n in range(1, 1001):
    s += n**n % cut
print(s)

end = time.time()
print(f"Program runtime: {end - start} seconds")
