# PROJECT EULER PROBLEM 090
import time
from itertools import combinations


def check(d_1, d_2):
    """ Checks if the dice d_1 and d_2 can display all squares. """
    if 6 in d_1:
        d_1.add(9)
    if 9 in d_1:
        d_1.add(6)
    if 6 in d_2:
        d_2.add(9)
    if 9 in d_2:
        d_2.add(6)
    for (a, b) in SQUARES:
        # Check if either (a, b) or (b, a) lie in (d_1, d_2).
        if not ((a in d_1 and b in d_2) or (a in d_2 and b in d_1)):
            return False
    return True


def fill(d_1, d_2):
    """ Fills d_1 and d_2 to contain 6 different digits each using
    'combinations' from itertools. """
    filled = []
    for digits_1 in combinations(DIGITS, 6):
        t_1 = d_1.union(set(digits_1))
        for digits_2 in combinations(DIGITS, 6):
            t_2 = d_2.union(set(digits_2))
            filled.append((t_1, t_2))
    return filled


start = time.time()

DIGITS = set(range(0, 10))
# Generate a list of all the squares, written as tuples (0, 1), (0, 4), etc.
SQUARES = [ (n**2 // 10, n**2 % 10) for n in range(1, 10)]
total = 0

filled = fill(set(), set())
for (d_1, d_2) in filled:
    if check(d_1, d_2):
        # The dice can be permuted, hence if they are different, they are being
        # counted twice. To take this into account, we add 2 to the total in
        # case they are equal, but then in the end we will divide by 2.
        if d_1 != d_2:
            total += 1
        else:
            total += 2

print(total // 2)

end = time.time()
print(f"Program runtime: {end - start} seconds")
