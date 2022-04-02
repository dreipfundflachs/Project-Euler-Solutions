###############################
#  PROJECT EULER PROBLEM 119  #
###############################

import time

def digital_sum(n: int) -> int:
    """ Determines the sum of all digits of n. """
    s = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        s += r
    return s


start = time.time()
special = []

for n in range(1, 100):
    for p in range(1, 100):
        power = n**p
        if digital_sum(power) == n and power > 9:
            special.append(power)
print(sorted(special)[29])


end = time.time()
print(f"Program runtime: {end - start} seconds")
