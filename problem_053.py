#################################
#  PROJECT EULER - PROBLEM 053  #
#################################
import time
from scipy.special import comb

start = time.time()

# A straightforward search, observing that the binomial coefficients
# binomial(n, k) and binomial(n, n - k) coincide, and that starting with k = 0,
# they increase with k until their maximum value, which occurs for k = k_max =
# n // 2, and then they start to decrease to 1 again for increasing k (except
# that binomial(n, k_max) = binomial(n, k_max + 1) when n is odd).
N = 10**6
MIN = 23
MAX = 100

count = 0
for n in range(MIN, MAX + 1):
    k = 1
    while comb(n, k) <= N:
        k += 1
    # By the observations above, if k_0 is the smallest integer such that
    # binomial (n, k_0) > N, then all values of k between k_0 and n - k_0
    # (including these) will also be greater than N.
    count += n - 2 * k + 1
print(count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
