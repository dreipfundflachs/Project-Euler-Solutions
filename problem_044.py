#################################
#  PROJECT EULER - PROBLEM 044  #
#################################
import time
from math import sqrt


def generate_pentagonals(n: int) -> list[int]:
    """ Generates a list containing all triangular numbers up to the n-th such
    number (notice that this triangular number will be n * (n + 1) // 2). """
    pentagonals = []
    for k in range(1, n + 1):
        pentagonal = k * (3 * k - 1) // 2
        pentagonals.append(pentagonal)

    return pentagonals


def is_pentagonal(n: int) -> bool:
    """ Decides whether n is a pentagonal number. """
    return ((sqrt(24 * n + 1) + 1) / 6.0).is_integer()


start = time.time()

N = 3000
pentagonals = generate_pentagonals(N)

active = True
for i in reversed(range(1, N)):
    if active is False:
        break
    else:
        for j in range(i + 1, N):
            # We want to check if pentagonals[j] is a sum of pentagonals[i]
            # with some other pentagonal complement, say, pentagonals[k].
            complement = pentagonals[j] - pentagonals[i]
            # And if the abs of the difference pentagonals[i] - pentagonals[k],
            # that is, pentagonals[i] - complement, is also pentagonal.
            difference = abs(pentagonals[i] - complement)
            if is_pentagonal(complement) and is_pentagonal(difference):
                print(difference)
                active = False
                break

end = time.time()
print(f"Program runtime: {end - start} seconds")
