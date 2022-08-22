#################################
#  PROJECT EULER - PROBLEM 058  #
#################################
import time
from random import randrange


def miller_rabin(n: int, k: int = 35) -> bool:
    """ Verifies whether a number n is prime using by using k random
    numbers between 2 and n - 1. Requires 'randrange' from the module 'random'.
    A good value for k in general is k = 40.
    """
    # The only even prime is 2:
    assert n >= 2
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


start = time.time()

# Choose a diagonal. Let n_1 be the first number != 1 along it and n_k be the
# number in the k-th position (other than 1).  Then
# n_k = n_(k-1) + (n_1 - 1) + 8*(k - 1) for k > 1.

M = 10**5

diagonals = [[]] * 4
diagonals[0] = [3]
diagonals[1] = [5]
diagonals[2] = [7]
diagonals[3] = [9]
relevant = [3, 5, 7]
d = [2, 4, 6, 8]


count = 3
for k in range(1, M):
    side_length = 1 + 2 * (k + 1)
    total = (2 * side_length) - 1
    for i in range(0, 3):
        diff = d[i]
        last = diagonals[i][-1]
        new = last + diff + 8 * k
        diagonals[i].append(new)
        relevant.append(new)
        if miller_rabin(new):
            count += 1
    if count / total < 0.100000:
        print(f"The total number of primes in a square of side {side_length}\n"
              f"is {count} out of a total of {total} numbers along the\n"
              f"diagonals, yielding the ratio {count/total}")
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
