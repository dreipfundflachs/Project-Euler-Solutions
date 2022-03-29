# PROJECT EULER PROBLEM 058
import time


def is_prime(n: int) -> bool:
    """ Verifies directly whether a number is prime. """
    if n % 2 == 0:
        return False
    else:
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True


start = time.time()

# Choose a diagonal. Let n_1 = be the first number != 1 along it and n_k be the
# number in the k-th position (other than 1).  Then
# n_k = n_(k-1) + (n_1 - 1) + 8*(k - 1) for k > 1.

diagonals = [[]] * 4
diagonals[0] = [3]
diagonals[1] = [5]
diagonals[2] = [7]
diagonals[3] = [9]
relevant = [3, 5, 7]
d = [2, 4, 6, 8]

M = 100_000

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
        if is_prime(new):
            count += 1
    if count / total < 0.100000:
        print(f"The total number of primes in a square of side {side_length}\n"
              f"is {count} out of a total of {total} numbers along the\n"
              f"diagonals, yielding the ratio {count/total}")
        break

end = time.time()
print(f"Program runtime is: {end - start} seconds")
