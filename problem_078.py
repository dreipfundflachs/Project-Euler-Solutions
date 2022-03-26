# PROJECT EULER PROBLEM 078
import time
from itertools import cycle, count


def pentagonal(n):
    return n * (3 * n - 1) // 2


def partition(n):
    global partitions
    if n <= 1:
        return 1
    if n not in partitions:
        signs = cycle([1, 1, -1, -1])
        pentagonals = [p for p in generalized_pentagonals if p <= n]
        partitions[n] = sum(sign * partition(n - p) \
                for sign, p in zip(signs, pentagonals)) % 10**6

    return partitions[n]


start = time.time()

P = 250
partitions = {0: 1, 1: 1}
generalized_pentagonals = \
        sorted([ k * (3 * k - 1)//2 for k in range(-P, P) if k != 0])

print(next((n for n in count(0) if partition(n) == 0)))

end = time.time()


print(f"Program runtime is: {end - start} seconds")

