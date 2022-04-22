#################################
#  PROJECT EULER - PROBLEM 045  #
#################################
import time


start = time.time()

N = 10**6
MINIMUM = 40755

# Notice that the pentagonal and hexagonal numbers increase more rapidly than
# the triangular numbers (i.e., the steps between consecutive numbers in the
# sequence are larger for the former types). Using this observation, the
# idea is to generate the triangular, pentagonal and hexagonal numbers on the
# fly, but to only update the pentagonal and hexagonal numbers if necessary,
# i.e., when the current pentagonal (resp. hexagonal) number gets overtaken by
# the current triangular number. This minimizes the number of comparisons we
# need to make.

t, p, h = 1, 1, 1  # First triangular, pentagonal and hexagonal number.
j = 1  # Will be used to generate the pentagonal numbers.
k = 1  # Will be used to generate the hexagonal numbers.

for i in range(2, N):
    t = i * (i + 1) // 2

    if t > p:
        j += 1
        p = j * (3 * j - 1) // 2

    if t > h:
        k += 1
        h = k * (2 * k - 1)

    if t == p == h and t > MINIMUM:
        print(t)
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
