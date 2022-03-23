# PROJECT EULER PROBLEM 074
import time


def factorial_digits(n):
    """ Calculates the sum of the factorials of all digits of n. """
    digits = []
    while n != 0:
        d = n % 10
        n = n // 10
        digits.append(d)
    s = 0
    for d in digits:
        s += facts[d]
    return s


start = time.time()

facts = {
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880,
        }

chains = {}
N = 10**6
special = 0

for n in range(N):
    start_value = n
    if start_value not in chains:
        chain_length = 0
        temp_chain = []
        while (n not in temp_chain) and (n not in chains):
            temp_chain.append(n)
            chain_length += 1
            n = factorial_digits(n)

        if n in chains:
            chain_length += chains[n]

        for i, k in enumerate(temp_chain):
            chains[k] = chain_length - i

        if chain_length == 60:
            special += 1

print(special)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
