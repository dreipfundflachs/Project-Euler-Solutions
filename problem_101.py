# PROJECT EULER PROBLEM 101
import time
from operator import mul
from functools import reduce


def p(n: int) -> int:
    """ This is the polynomial described at the end of the problem's statement,
    considered as a function.  """
    monomials = [(-1)**k * n**k for k in range(11)]     # Monomials of p(n)
    return sum(monomials)


def lagrange_interpolation(f, c: list[float], x: float) -> float:
    """ Yields the value at x of the Lagrange polynomial (interpolation) of a
    function f, based on the data points contained in the list c of length > 1.
    """
    d = len(c) - 1  # Degree of the interpolation polynomial
    # The polynomial is a sum of (d + 1) terms, each having the form:
    # f(c_k) * (x - c_0) * ... * {(x - c_k)} * ... * (x - c_d)
    # divided by (c_k - c_0) * ... * {(c_k - c_k)} * ... * (c_k - c_d),
    # for k = 0, ..., d, where the {} denote that the expression inside 
    # should be omitted.

    # Initialize lists to hold each of the numerators, denominators and
    # complete expressions described in the preceding paragraph.
    numerators = [0] * (d + 1)
    denominators = [0] * (d + 1)
    summands = [0] * (d + 1)
    # Compute them for k = 0, ..., d and return their sum.
    for k in range(d + 1):
        numerators[k] = reduce(mul, [(x - c[i]) for i in
                                     range(d + 1) if i != k])
        denominators[k] = reduce(mul, [(c[k] - c[i]) for i in
                                       range(d + 1) if i != k])
        summands[k] = f(c[k]) * numerators[k] / denominators[k]
    return sum(summands)


start = time.time()

N = 10
fits = [1, ]
# For each degree d = 1, ..., N - 1, calculate the Lagrange interpolation of p
# at (d + 2) (called guess below) and, if it does not agree with the actual
# value of p(d + 2), append it to the least of FITs.
for d in range(1, N):
    c = [k for k in range(1, d + 2)]
    guess = lagrange_interpolation(p, c, d + 2)
    if guess != p(d + 2):
        fits.append(guess)

print(sum(fits))

end = time.time()
print(f"Program runtime is: {end - start} seconds")
