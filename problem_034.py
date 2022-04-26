#################################
#  PROJECT EULER - PROBLEM 034  #
#################################
import time
from math import factorial


def is_sum_of_digit_factorials(n: int) -> bool:
    """ Decides whether an integer > 2 is the sum of the factorials of its
    digits. """
    digits_of_n = [int(digit) for digit in str(n)]
    sum_of_factorials_of_digits = 0
    for digit in digits_of_n:
        sum_of_factorials_of_digits += FACTORIAL_LIST[digit]
    if sum_of_factorials_of_digits == n:
        return True
    else:
        return False


start = time.time()

FACTORIAL_LIST = [factorial(k) for k in range(0, 10)]

# Find the least integer N such that 10**N > (9!) * N. If a number is greater
# than N * (9!), then it will certainly be greater than the sum the
# factorials of its digits.
for n in range(1, 10):
    if 10**n > factorial(9) * n:
        N = n
        break

answer = 0
for n in range(3, N * FACTORIAL_LIST[9]):
    if is_sum_of_digit_factorials(n):
        answer += n

print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
