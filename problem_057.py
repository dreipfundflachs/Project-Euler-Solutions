#################################
#  PROJECT EULER - PROBLEM 057  #
#################################
import time


def get_number_of_digits(n: int) -> int:
    """ Determines the number digits of n. """
    d = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        d += 1
    return d


start = time.time()

N = 10**3

p = [3]
q = [2]
count = 0  # Counts the number of fractions satisfying the stated condition.

for k in range(1, N):
    # It is easy to prove by induction the following recursive formulae for
    # the numerators and denominators:
    current_p = p[k - 1] + 2 * q[k - 1]
    current_q = p[k - 1] + q[k - 1]
    p.append(current_p)
    q.append(current_q)
    if get_number_of_digits(current_p) > get_number_of_digits(current_q):
        count += 1

print(count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
