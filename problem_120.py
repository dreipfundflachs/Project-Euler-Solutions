# PROJECT EULER - PROBLEM 120
import time

start = time.time()
# The problem becomes quite easy with the appropriate mathematical background.
# Notice that using binomial expansion, (a - 1)**n + (a + 1)**n equals
# [1 + (-1)**n] + n * a * [1 - (-1)**n] + {other terms divisible by a**2}.
# Hence, the remainder upon division by a**2 equals 2 if n is even and 2 * a * n
# (mod a**2) if n is odd. 

# Now the numbers of the form 2 * a * n where n is odd can be more conveniently
# expressed in the form (4 * k + 2) * a where k >= 0 is arbitrary. The possible
# remainders r upon division by a **2 are: 0 * a, 1 * a, ..., (a - 1) * a. Let
# us try to find out when the maximum possible remainder (a - 1) * a can be
# realized.

# For this to hold, we need that (4 * k + 2) * a = (a - 1) * a (mod a**2), that
# is, (4 * k + 3) * a = 0 (mod a**2). If a is _odd_, then 4 is a unit in
# Z/(a**2), that is, we can choose k_0 such that 4 * k_0 = 1 (mod a**2) and
# then take k = k_0 + (a - 1) - 3 to realize the maximum possible remainder.

# On the other hand, if a is even, then a**2 cannot divide (4 * k + 3) * a,
# since if m is the largest power of 2 dividing a, the largest power of 2
# dividing (4 * k + 3) * a is also m, while for a**2 this largest power is 
# 2 * m.

# Hence if a is even, we attempt to realize the second largest possible
# remainder, namely, (a - 2) * a. We have (4 * k + 2) * a = (a - 2) * a (mod
# a**2) if and only if 4 * (k + 1) * a = 0 (mod a**2) for some k. Since k is
# arbitrary, we can take for example k = a - 1 to find a solution.

# In conclusion: If a is even, the largest possible remainder is a * (a - 2),
# while if a is odd, the largest possible remainder is a * (a - 1).

N = 1000
total = 0

for a in range(3, N + 1):
    current_remainders = []
    if a % 2 == 0:
        r = a * (a - 2)
    if a % 2 == 1:
        r = a * (a - 1)
    total += r
print(total)

end = time.time()
print(f"Program runtime: {end - start} seconds")
