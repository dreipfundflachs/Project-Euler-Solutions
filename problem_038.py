###############################
#  PROJECT EULER - PROBLEM 038  #
###############################

import time


def is_pandigital(s):
    "Decides whether a number string is 1-to-9 pandigital."
    digits = set(range(1, 10))
    digits_in_number = set([int(k) for k in s])
    boolean = (digits_in_number == digits)
    return boolean


start = time.time()

# Initialize the maximum product (m), the maximum base used in the product
# (base) and the number of factors used to multiply the product(mn)

m = 1
mbase = 1
mn = 1

# Loop through all numbers having less than 5 digits, multiplying them by
# chains of length n, and test whether the result is pandigital. If it is,
# update the maxima if necessary.

for base in range(10**4):
    concat = ''
    for n in range(1, 10):
        concat += str(base * n)
        if len(concat) > 9:
            break
        if len(concat) == 9 and is_pandigital(concat):
            p = int(concat)
            if p > m:
                m = p
                mbase = base
                mn = n
                break

print(mbase, mn, m)

end = time.time()
print(f"Program runtime: {end - start} seconds")
