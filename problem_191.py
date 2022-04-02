# PROJECT EULER PROBLEM 191
import time

# This problem can easily be solved by finding recursive formulas for the
# number of prize strings, if one separates them by types depending on their
# last element. It is possible to define five functions which compute the
# number of prize strings ending in O, A and not containing L, ending in L, or
# ending in O, A and containing L, if one allows for a depth of 2. (More
# explicitly, the formula for the number of strings of length n ending in A and
# containing L involves the number of strings of length n - 2 ending in O and
# containing L). However, although this recursive approach works well for small
# n, for n close to 25 it already takes more than 1 second, because the values
# needed are calculated multiple times (that is, there are many function calls
# which could be avoided by storing the results of previous computations).

# A more efficient approach, which still relies on the same idea, is to find
# recursive formulas of depth 1. In this case, we can conveniently store the
# result of the previous computation in a list, and work directly with that
# list to avoid repeated calls to the recursive functions. This is what we do
# below. In any case, we leave the recursive formulas in function definitions
# at the beginning for clarity. The reader will easily be able to prove the
# validity of the formulas.


def s_O(n):
    """ Computes the number of strings of length n which end in an 'O' and do
    not contain the letter 'L'. """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (s_O(n - 1) + s_A(n - 1) + s_AA(n - 1))


def s_A(n):
    """ Computes the number of strings of length n which end in an 'A', but not
    in 'AA', and that do not contain the letter 'L'. """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return s_O(n - 1)


def s_AA(n):
    """ Computes the number of strings of length n which end in 'AA',
    but do not contain the letter 'L'. """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return s_A(n - 1)


def s_L(n):
    """ Computes the number of strings of length n which end in an 'L'. """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (s_O(n - 1) + s_A(n - 1) + s_AA(n - 1))


def s_O_contains_L(n):
    """ Computes the number of strings of length n which end in an 'O' and
    which contain the letter 'L'. """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (s_O_contains_L(n - 1) + s_A_contains_L(n - 1) +
                + s_AA_contains_L(n - 1) + s_L(n - 1))


def s_A_contains_L(n):
    """ Computes the number of strings of length n which end in an 'A', but not
    in 'AA', and which contain the letter 'L'. """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return s_O_contains_L(n - 1) + s_L(n - 1)


def s_AA_contains_L(n):
    """ Computes the number of strings of length n which end in 'AA' and
    which contain the letter 'L'. """
    if n == 1:
        return 0
    elif n == 2:
        return 0
    else:
        return s_A_contains_L(n - 1)


if __name__ == "__main__":

    start = time.time()

    N = 30
    s = [0] * 7     # List containing the various types of prize strings.
    s[0] = s_O(4)
    s[1] = s_A(4)
    s[2] = s_AA(4)
    s[3] = s_L(4)
    s[4] = s_O_contains_L(4)
    s[5] = s_A_contains_L(4)
    s[6] = s_AA_contains_L(4)

    # Use a temporary list 't' to hold the results of computation in each
    # step.
    t = [0] * 7
    # The formulas below mimic the function definitions above in list format.
    for n in range(5, N + 1):
        t[0] = s[0] + s[1] + s[2]
        t[1] = s[0]
        t[2] = s[1]
        t[3] = s[0] + s[1] + s[2]
        t[4] = s[3] + s[4] + s[5] + s[6]
        t[5] = s[4] + s[3]
        t[6] = s[5]
        s = t[:]

    # Print the answer.
    print(sum(t))

    end = time.time()
    print(f"Program runtime: {end - start} seconds")
