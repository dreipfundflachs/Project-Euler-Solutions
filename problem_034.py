#################################
#  PROJECT EULER - PROBLEM 034  #
#################################
import time
from math import factorial


def is_sum_of_digit_factorials(n: int) -> bool:
    """ Decides whether an integer > 2 is the sum of the factorials of its
    digits. """
    # Make a copy m of n and extract the digits of n by repeatedly dividing m
    # by 10, storing the remainders:
    sum_of_digit_factorials = 0
    m = n
    while m != 0:
        sum_of_digit_factorials += FACTORIALS[(m % 10)]
        m //= 10

    if sum_of_digit_factorials == n:
        return True
    else:
        return False


start = time.time()

FACTORIALS = [factorial(k) for k in range(0, 10)]

# Let N be the least integer such that 10**(N - 1) > (9!) * N. Then
#   10**(D - 1) > (9!) * D for all D >= N.
# If a number n is greater than (9!) * N, then either:
#   (1) n has D > N digits, hence n >= 10**(D - 1) > (9!) * D.
#   (2) n has exactly N digits, but the sum of the factorials of its digits
#       must be less than (9!) * N, which in turn is less than n by hypothesis.
# In any case, n will be greater than the sum of the factorials of its digits.

for n in range(1, 10):
    if 10**(n - 1) > FACTORIALS[9] * n:
        N = n
        break

answer = 0
for n in range(3, N * FACTORIALS[9]):
    if is_sum_of_digit_factorials(n):
        answer += n

print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
