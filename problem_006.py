#################################
#  PROJECT EULER - PROBLEM 006  #
#################################

# Note that the difference is the sum of
#   2 * a * b
# for a < b and both a, b between 1 and n.

import time


def get_difference_of_sums(n: int) -> int:
    """
    Calculates the difference between the square of the sum 1 + 2 + ... + n of
    all numbers between 1 and n and the sum 1**2 + 2**2 + ... + n**2 of the
    squares of all numbers between 1 and n.
    """
    difference = 0
    for a in range(1, n + 1):
        # The sum of all numbers b between (a + 1) and n equals:
        # (n + a + 1) * (n - a) / 2,
        # and we need to multiply this by 2 * a.
        difference += a * (n + a + 1) * (n - a)
    return difference


start = time.time()

print(get_difference_of_sums(100))

end = time.time()
print(f"Program runtime: {end - start} seconds")
