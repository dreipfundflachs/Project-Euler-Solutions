# PROJECT EULER PROBLEM 24
import time
from itertools import permutations


start = time.time()
digits = list(range(0, 10))
perms = list(permutations(digits))
number_string = map(str, perms[10**6 - 1])
number_string = ''.join(number_string)
number = int(number_string)
print(number)


end = time.time()
print(f"Program runtime is: {end - start} seconds")
