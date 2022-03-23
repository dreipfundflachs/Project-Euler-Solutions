# PROJECT EULER PROBLEM 046
import time
from project_euler import prime_sieve, is_square

start = time.time()

primes = prime_sieve(10**4)
set_of_primes = set(primes)
numbers = set(range(3, 10**4, 2)).difference(set_of_primes)
special = []
print(numbers)

for n in numbers:
    flag = False
    for p in primes:
        if p > n:
            special.append(n)
            break
        d = (n - p)//2
        flag = is_square(d)
        if flag:
            break

print(special)
end = time.time()
print(f"Program runtime is: {end - start} seconds")
