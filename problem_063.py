#################################
#  PROJECT EULER - PROBLEM 063  #
#################################
import time


start = time.time()

N = 10

count = 0  # Counts the number of integers satisfying the stated condition.

# If a number k is > 10, then certainly k**n will have more than n digits.  On
# the other hand, for a number k between 1 and 9, it is clear that k**1 = k has
# 1 digit and that eventually k**n will have fewer than n digits. If this
# happens first for some n_0, then for no value n > n_0 will k**n have n
# digits. Thus we can count these numbers as follows:
for k in range(1, N):
    n = 1
    while len(str(k**n)) == n:
        count += 1
        n += 1

print(count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
