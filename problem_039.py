#################################
#  PROJECT EULER - PROBLEM 039  #
#################################
import time
from math import isqrt


start = time.time()

N = 1000

solutions = {k: 0 for k in range(1, N + 1)}

# Denote the smaller leg by a, the larger one by b and the hypothenuse by c.
# Count the number of solutions for each perimeter between 1 and N.
for a in range(1, N // 3):
    for b in range(a + 1, N):
        sum_of_squares = a**2 + b**2
        c = isqrt(sum_of_squares)
        if a + b + c > N:
            break
        elif c**2 == sum_of_squares:
            solutions[a + b + c] += 1

# Search for the perimeter for which the # of solutions is maximized.
max_number_of_solutions = 0
maximizing_perimeter = 0
for perimeter in range(1, N + 1):
    number_of_solutions = solutions[perimeter]
    if number_of_solutions > max_number_of_solutions:
        max_number_of_solutions = number_of_solutions
        maximizing_perimeter = perimeter

print(maximizing_perimeter)

end = time.time()
print(f"Program runtime: {end - start} seconds")
