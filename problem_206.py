# PROJECT EULER PROBLEM 206
import time
from math import isqrt


def small_is_special(n):
    s = (str(n))[-10:]
    if int(s[8]) == 0:
        for k in reversed(range(0, 4)):
            if int(s[2*k]) != k + 6:
                return False
    return True


def is_special(n):
    """ Decides whether a number having 19 digits (or 18, or more)
    has the required form. """
    s = str(n)
    if int(s[18]) == 0:
        for k in reversed(range(0, 9)):
            if int(s[2*k]) != k + 1:
                return False
    return True


start = time.time()

small_special = []
print(small_is_special(607080900))
m_1 = isqrt(607080900)

for k in range(m_1, 10**9):
    if small_is_special(k):
        small_special.append(k)

print(small_special)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
