# PROJECT EULER PROBLEM 043
import time
from itertools import permutations


def has_property(digits):
    primes = [1, 2, 3, 5, 7, 11, 13, 17]
    for i in range(1, len(digits) - 2):
        if not int(''.join(digits[i:i+3])) % primes[i] == 0:
            return False
    return True


def convert_list_to_int(lst):
    return int(''.join(str(i) for i in lst))


start = time.time()

pandigitals = permutations((str(i) for i in range(0, 10)))
print(sum(convert_list_to_int(p) for p in pandigitals if has_property(p)))

end = time.time()
print(f"Program runtime: {end - start} seconds")
