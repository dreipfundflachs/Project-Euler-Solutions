# PROJECT EULER - PROBLEM 056
import time


def get_digital_sum(n):
    """ Determines the sum of all digits of n. """
    s = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        s += r
    return s


start = time.time()

# A direct approach works.
m = 1
for a in range(1, 100):
    for b in range(1, 100):
        s = get_digital_sum(a**b)
        if s > m:
            m = s
            ma = a
            mb = b

print(ma, mb, m)

end = time.time()
print(f"Program runtime: {end - start} seconds")
