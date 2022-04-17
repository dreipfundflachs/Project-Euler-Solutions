#################################
#  PROJECT EULER - PROBLEM 024  #
#################################
import time
from itertools import permutations


start = time.time()

N = 10**6
DIGITS = list(range(0, 10))
DIGIT_PERMUTATIONS = list(permutations(DIGITS))

number_strings = [str(k) for k in DIGIT_PERMUTATIONS[N - 1]]
answer = int(''.join(number_strings))
print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
