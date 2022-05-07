#################################
#  PROJECT EULER - PROBLEM 065  #
#################################
import time
from fractions import Fraction


def get_digital_sum(n: int) -> int:
    """ Determines the sum of all digits of n. """
    s = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        s += r
    return s


def continued(coefficients: list[int]) -> int:
    """ Computes the value of the continued fraction whose coefficients are
    given, as a rational number.
    Requires: 'Fraction' from module 'fractions'. """
    m = len(coefficients)
    if m == 1:
        x = Fraction(1, coefficients[0])
    else:
        last = coefficients.pop()
        next_to_last = coefficients.pop()
        new_last = Fraction(last * next_to_last + 1, last)
        coefficients.append(new_last)
        x = continued(coefficients)
    return x


start = time.time()

N = 99
coefficients = []

for k in range(N):
    if k % 3 == 1:
        i = (k - 1) // 3 + 1
        coefficients.append(2 * i)
    else:
        coefficients.append(1)

# Determine the numerator by adding 2 to the ``fractional part''.
num = (continued(coefficients) + 2).numerator
print(get_digital_sum(num))

end = time.time()
print(f"Program runtime: {end - start} seconds")
