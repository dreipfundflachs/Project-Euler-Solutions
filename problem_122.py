# PROJECT EULER PROBLEM 122
import time
from itertools import combinations_with_replacement as cwr


def bound(n: int) -> int:
    """ Returns the value of the number of multiplications required to produce
    the exponent n using the 'binary method' described in the statement. """
    greatest_power = len(bin(n)) - 3
    r = bin(n).count('1') - 1
    return greatest_power + r



start = time.time()

N = 200
# ms[n] equals m(n).
ms = {0: 0, 1: 0}
ms = fill(ms)
print(ms)
print(ms[15])

total = sum([ms[k] for k in range(1, N + 1)])
print(total)
print(sum([bound(k) for k in range(1, N + 1)]))


end = time.time()
print(f"Program runtime is: {end - start} seconds")

# Here is an initial failed attempt using dynamic programming
# which gives a wrong answer 1584, off by 2. 
def fill(ms) -> int:
    """ Returns the value of the function m(n) described in the statement. """
    dynamic = [[] for k in range(N + 1)]
    dynamic[0].append({1})
    # dynamic[k] holds a list consisting of all the sets obtained using up to m
    # multiplications, e.g., dynamic[0] = [{1}], dynamic[1] = [{1, 2}],
    # dynamic[2] = [{1, 2, 4}, {1, 2, 3}], etc...
    for k in range(1, N + 1):
        for current_set in dynamic[k - 1]:
            for (a, b) in cwr(current_set, 2):
                new_set = current_set.copy()
                r = a + b
                if r < N + 1 and ms.get(r) is None:
                    ms[r] = k
                    new_set.add(r)
                    if new_set not in dynamic[k]:
                        dynamic[k].append(new_set)
    return ms

# Uncomment the three lines below to print the (wrong!) answer obtained by
# using the 'fill' function above.

# ms = {0: 0, 1: 0}
# ms = fill(ms)
# print(sum([ms[k] for k in range(1, N + 1)]))


