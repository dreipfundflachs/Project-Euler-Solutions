# PROJECT EULER PROBLEM 085
import time


def number_of_subrectangles(m, n):
    """ Returns the number of subrectangles in a rectangular grid of dimensions
    m x n. There are (m + 1) * (n + 1) vertices in total. To determine a
    subrectangle, one first selects one of these vertices, and then any other
    vertice not on the same line or column, which will determine a diagonal of
    the rectangle, hence prescribes the rectangle uniquely. For the latter
    there are thus [(m + 1) * (n + 1) - m - n - 1] = m * n possibilities. Also,
    one can permute the two vertices or select the two vertices in the other
    diagonal while also determining the same rectangle, so we need to divide
    this by 2 * 2 = 4. """

    return int((m * n + m + n + 1) * m * n // 4)


start = time.time()

# Initializing the parameters, the difference, and the solutions
c = 2 * (10 ** 6)
diff = c
special_m = 0
special_n = 0

# Find the solution by updating the error whenever it decreases.
for m in range(1, 100):
    for n in range(1, 100):
        curr_diff = abs(c - number_of_subrectangles(m, n))
        if curr_diff < diff:
            diff = curr_diff
            special_m = m
            special_n = n

# Print the solution
print(special_m, special_n, special_m * special_n)
print(number_of_subrectangles(special_m, special_n), diff)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
