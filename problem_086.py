# PROJECT EULER PROBLEM 086
import time
from math import isqrt

start = time.time()

# We seek triples (a, b, c) such that c <= a <= b. Notice that the three
# possible shortest paths have lengths sqrt(a**2 + (b + c)**2), 
# sqrt(b**2 + (a + c)**2) and sqrt(c**2 + (a + b)**2). Clearly, of these three
# the shortest one is the first. To loop only twice, we set d = b + c and first
# find the pairs (a, d) for which a**2 + d**2 is a perfect square. We then
# filter these pairs to obtain b, c such that 0 < c <= b <= a.
n = 0
pairs = []
total = 0
while total < 10**6:
    new_pairs = []
    n += 1
    a = n
    # Find all Pythagorean pairs (a, d = b + c) with a the current value of a.
    # The other values, with a < n, have already been found. Notice that since
    # c <= b <= a, d = b + c must be less than 2 * a + 1.
    for d in range(2, 2 * a + 1):
        s = a**2 + d**2
        # Check if s is a perfect square.
        if isqrt(s)**2 == s:
            new_pairs.append((a, d))

    pairs += new_pairs
    for (a, d) in new_pairs:
        # b must lie between 1 and a.
        for b in range(1, a + 1):
            # c = d - b must lie between 1 and b.
            c = d - b
            if 0 < c and c <= b:
                total += 1

print(n, total)

end = time.time()
print(f"Program runtime: {end - start} seconds")
