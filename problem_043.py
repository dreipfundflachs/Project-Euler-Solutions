#################################
#  PROJECT EULER - PROBLEM 043  #
#################################
import time
from itertools import permutations


def is_substring_divisible(digits: list[str]) -> bool:
    PRIMES = [1, 2, 3, 5, 7, 11, 13, 17]
    for i in range(1, len(digits) - 2):
        if int(''.join(digits[i:i + 3])) % PRIMES[i] != 0:
            return False
    return True


def convert_list_of_digits_to_int(lst: list[str]) -> int:
    return int(''.join(str(i) for i in lst))


start = time.time()

PANDIGITALS = permutations((str(digit) for digit in range(0, 10)))
print(sum(convert_list_of_digits_to_int(pandigital) for pandigital
          in PANDIGITALS if is_substring_divisible(pandigital)))

end = time.time()
print(f"Program runtime: {end - start} seconds")
