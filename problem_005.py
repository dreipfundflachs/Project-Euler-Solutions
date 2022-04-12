#################################
#  PROJECT EULER - PROBLEM 005  #
#################################
import time


"""
By the prime factorization theorem (a.k.a. the fundamental theorem of
arithmetic), a number will be divisible by all numbers between 1 and N if
and only if it is divisible by p_1**e_1 * ... * p_r**e_r, where:
    (i) p_1, ..., p_r are all primes less than or equal to N;
    (ii) e_i is the largest exponent such that p_i**e_i <= N (i = 1, ..., r).

In our case N = 20, hence the answer is:
    smallest = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
"""

start = time.time()

SMALLEST = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
print(SMALLEST)

end = time.time()
print(f"Program runtime: {end - start} seconds")
