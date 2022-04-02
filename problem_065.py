# PROJECT EULER PROBLEM 065
import time
from project_euler import get_digital_sum


def continued(coefficients):
    """ Computes the value of the continued fraction whose
    coefficients are given, as a rational number.
    """
    from fractions import Fraction
    m = len(c)
    if m == 1:
        x = Fraction(1, c[0])
    else:
        last = coefficients.pop()
        next_to_last = coefficients.pop()
        new_last = Fraction(last * next_to_last + 1, last)
        coefficients.append(new_last)
        x = continued(coefficients)
    return x


start = time.time()
# Initialize the list of coefficients.
n = 99
c = []
for k in range(n):
    if k % 3 == 1:
        i = (k - 1) // 3 + 1
        c.append(2*i)
    else:
        c.append(1)

# Determine the numerator by adding 2 to the ``fractional part''.
nm = (continued(c) + 2).numerator
print(nm)
print(get_digital_sum(nm))


end = time.time()
print(f"Program runtime: {end - start} seconds")
