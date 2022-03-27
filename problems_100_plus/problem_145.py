# PROJECT EULER PROBLEM 145
import time

start = time.time()

# The formulas below were obtained by using pen and paper.
def reversible(d):
    """ Yields the number of reversible numbers having exactly d digits (with
    0 being excluded as a possibility for the leading and trailing digits)."""
    if d  == 1:
        return 0
    elif d == 2:
        return 10 * 2
    elif d == 3:
        return 5 * 10 * 2
    elif d > 3 and d % 2 == 0:
        return 30 * reversible(d - 2)
    elif d > 3 and d % 2 != 0:
        return 25 * 20 * reversible(d - 4)


N = 9
total = 0
for d in range(1, N + 1):
    total += reversible(d)

print(total)
end = time.time()
print(f"Program runtime is: {end - start} seconds")
