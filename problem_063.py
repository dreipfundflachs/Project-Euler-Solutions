# PROJECT EULER PROBLEM 063
import time


def number_of_digits(n):
    """ Returns the number of digits of an integer n expressed in base 10. """
    d = len(str(n))
    return d


start = time.time()

s = 0
for n in range(1, 10):
    m = 1
    while number_of_digits(n**m) == m:
        s += 1
        m += 1

print(s)

end = time.time()
print(f"Program runtime: {end - start} seconds")
