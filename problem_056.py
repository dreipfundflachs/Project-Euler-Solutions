#################################
#  PROJECT EULER - PROBLEM 055  #
#################################
import time


def get_digital_sum(n):
    """ Determines the sum of all digits of n. """
    digital_sum = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        digital_sum += r

    return digital_sum


start = time.time()

# A direct approach works.
N = 100

max_digital_sum = 1
for a in range(1, N):
    for b in range(1, N):
        digital_sum = get_digital_sum(a**b)
        if digital_sum > max_digital_sum:
            max_digital_sum = digital_sum
            max_a, max_b = a, b

print(f"The maximum digital sum is {max_digital_sum}, "
      f"which is attained for a = {max_a} and b = {max_b}.")

end = time.time()
print(f"Program runtime: {end - start} seconds")
