#################################
#  PROJECT EULER - PROBLEM 074  #
#################################
import time


def get_sum_of_digit_factorials(n: int) -> int:
    """ Calculates the sum of the factorials of all digits of n. """
    sum_of_factorials = 0
    while n != 0:
        d = n % 10
        n = n // 10
        sum_of_factorials += FACTORIALS[d]
    return sum_of_factorials


start = time.time()

N = 10**6
FACTORIALS = [
        1,  # factorial of 0;
        1,
        2,
        6,
        24,
        120,
        720,
        5040,
        40320,
        362880  # factorial of 9
        ]

chains = {}  # chains[k] will store the chain length of k.
answer = 0

for n in range(N):
    start_value = n
    # For each n <= N, we first check whether its chain length has already been
    # computed:
    if start_value not in chains:
        # If not, we set its chain length to 0 and determine all members of
        # its chain, storing them in the list 'temp_chain'.
        chain_length = 0
        temp_chain = []
        # At each step, update n to the sum of the factorials of the digits of
        # the previous value of n (i.e., the last member of temp_chain); if
        # this newest number has already appeared in the chain, or if its chain
        # length is already known, then stop.
        while n not in temp_chain and n not in chains:
            temp_chain.append(n)
            chain_length += 1
            n = get_sum_of_digit_factorials(n)
        # If the preceding loop was terminated because the chain length of n
        # had already been computed, we add that value to our chain length
        # variable; otherwise, it is not modified.
        if n in chains:
            chain_length += chains[n]
        # Next, for each member of the chain of the starting value, we compute
        # its chain length using the chain length of its last member, n.
        for i, k in enumerate(temp_chain):
            chains[k] = chain_length - i
        # If the chain length of n equals 60, increment the answer by 1.
        if chain_length == 60:
            answer += 1

print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
