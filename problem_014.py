#################################
#  PROJECT EULER - PROBLEM 014  #
#################################
import time


def collatz_function(n: int) -> int:
    """ Computes the value of the Collatz function on a positive integer n. """
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n + 1)


start = time.time()

N = 10**6

collatz_chain_lengths = {1: 1}
max_count = 1
max_number = 1

for n in reversed(range(2, N)):
    if n in collatz_chain_lengths:
        continue
    # If the length of the Collatz chain of n has not yet been computed, we
    # will keep iterating the Collatz function on n and storing the
    # intermediate numbers in a list until we finally reach a terminal number
    # whose Collatz chain-length has already been computed. The chain length of
    # the Collatz sequence of all intermediate numbers can be computed by
    # adding their position in the reversed list to the chain-length of the
    # terminal number.
    else:
        numbers = [n]
        k = n
        while k not in collatz_chain_lengths:
            k = collatz_function(k)
            numbers.append(k)
        base_length = collatz_chain_lengths[k]
        for i, number in enumerate(reversed(numbers)):
            collatz_chain_lengths[number] = base_length + i

    if collatz_chain_lengths[n] > max_count:
        max_count = collatz_chain_lengths[n]
        max_number = n

print(max_number)

end = time.time()
print(f"Program runtime: {end - start} seconds")
