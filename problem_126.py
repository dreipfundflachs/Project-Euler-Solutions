#################################
#  PROJECT EULER - PROBLEM 126  #
#################################
import time

# To deduce the formula below, fist consider the analogous problem in 2
# dimensions, i.e., consider the number of squares in the n-th layer (n >= 1)
# of a covering of a rectangle of dimensions a <= b . One proves easily by
# induction that it is given by:
# cover(a, b, n) = 2(a + b) + 4 * (n - 1)

# Using the same reasoning, one again sees by induction that the number of
# cubes in the n-th layer (n >= 1) of the covering of a cuboid of dimensions
# a <= b <= c is given by:
# cover(a, b, c, n) = 2 * (a * b + a * c + b * c)
#                   + 4 * (n - 1) * (a + b + c + n - 2)


# This function is not actually used below.
def cover(a: int, b: int, c: int, n: int) -> int:
    """ Computes the number of unit cubes in the n-th layer in the covering of
    an original cuboid of dimensions a, b and c. """
    if n >= 1:
        cubes = 2 * (a * b + a * c + b * c) + 4 * (n - 1) * (a + b + c + n - 2)
        return cubes


def cover_fill(a: int, b: int, c: int) -> None:
    """ For each n >= 1, computes the number of cubes in the n-th layer of the
    covering of an original cuboid of dimensions (a, b, c), as long as this
    number is at most C, and updates the number of covers having each count
    that comes up in the computation. """
    global covers
    base = 2 * (a * b + a * c + b * c)  # cubes in the 1st layer
    covers[base] += 1
    # The difference between the number of cubes in the n-th and (n - 1)-th
    # layer for n >= 2 is given by 4 * (a + b + c + 2 * (n - 2)). To avoid
    # repeated computations, we just update the previous value accordingly.
    current_cover = base
    n = 2
    while current_cover + 4 * (a + b + c + 2 * (n - 2)) <= C:
        current_cover += 4 * (a + b + c + 2 * (n - 2))
        covers[current_cover] += 1
        n += 1
    return None


start = time.time()
# C is the maximum number of cubes that will be stored. The specific value
# below was chosen _after_ the solution was found, to decrease runtime.
C = 2 * 10**4
# covers[n] will store the number of cuboids which give rise to a collection of
# n cubes at some stage (layer).
covers = {}

# In computing the covers, we take a <= b <= c and only consider those counts
# which are smaller than C. Thus, for example, we must have 2 * (3 * a**2) <=
# C, or a <= C / 6.
for k in range(C + 1):
    covers[k] = 0
for a in range(1, C // 6 + 1):
    for b in range(a, C + 1):
        if (2 * a * b + b**2) > C / 2:
            break
        else:
            for c in range(b, C + 1):
                if (2 * (a * b + a * c + b * c) > C):
                    break
                else:
                    cover_fill(a, b, c)

for n in range(C + 1):
    if covers[n] == 1000:
        print(n)
        break
end = time.time()
print(f"Program runtime: {end - start} seconds")
