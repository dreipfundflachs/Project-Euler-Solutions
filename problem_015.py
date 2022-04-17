#################################
#  PROJECT EULER - PROBLEM 015  #
#################################
import time
from math import factorial


start = time.time()

# Out of 40 total moves, we need to choose 20 of them to be from left to right,
# and this completely determines the route.  Hence, the answer is the binomial
# coefficient (40, 20) = 40! / (20!)**2. More generally, for an M x N grid,
# the number of routes is given by the binomial coefficient (M + N, N).

M = 20
N = 20

a = factorial(M + N)
b = factorial(N)
number_of_routes = a // (b**2)

print(number_of_routes)

end = time.time()
print(f"Program runtime: {end - start} seconds")
