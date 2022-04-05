#################################
#  PROJECT EULER - PROBLEM 135  #
#################################
import time

# If z, y, x are consecutive terms of an arithmetic progression, then we may
# write y = z + a and x = z + 2a for some a > 0, and then the original equation
# can be rewritten, after some simplification, as (3 * a - z) * (z + a) = n.
# The only requirements are that a, z and n > 0.

start = time.time()
N = 10**6

# solution_count[n] will store the number of solutions to the equation for
# fixed n.
solution_count = {n: 0 for n in range(N + 1)}
for z in range(1, N + 1):
    # If 3 * a - z <= 0, then certainly these values of a and z will not yield
    # a solution, since the product (3 * a - z) * (z + a) = n will be <= 0.
    for a in range(z // 3 + 1, N + 1):
        n = (z + a) * (3 * a - z)
        if n >= N:
            break
        else:
            solution_count[n] += 1

print(len([n for n in range(N + 1) if solution_count[n] == 10]))

end = time.time()
print(f"Program runtime: {end - start} seconds")
