#################################
#  PROJECT EULER - PROBLEM 073  #
#################################
import time


def gcd(a: int, b:  int) -> int:
    """ Computes the greatest common divisor (gcd) of integers a and b. """
    while b:
        a, b = b, a % b
    return a


start = time.time()

N = 12 * 10**3

count = 0
# For each possible denominator q, and for each numerator p such that p / q
# lies between 1/3 and 1/2, verify whether p / q is a reduced fraction; if so,
# increase the count by 1.
for q in range(4, N + 1):
    for p in range((q // 3) + 1, (q // 2) + 1):
        if gcd(q, p) == 1:
            count += 1

print(count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
