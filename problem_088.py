#################################
#  PROJECT EULER - PROBLEM 088  #
#################################
import time
from math import log, prod


# The solution is based on the following observations:
#
#   (i) Let n be a product-sum number whose factors >= 2 are b_1, ..., b_r.
#   Then the number of ones in the decomposition must be:
#           b_1 * ... * b_r - (b_1 + ... + b_r),
#   for a total of
#           k = b_1 * ... * b_r - (b_1 + ... + b_r) + r
#   factors (including the ones).
#
#   (ii) Conversely, given b_1, ..., b_r, all >= 2, their product n is greater
#   to or equal to their sum. Thus we can make n a product-sum number by adding
#   some 1 factors if necessary, the quantity of ones being as in (i).
#
#   (iii) A _minimal_ product-sum number involving k factors/summands must
#   be <= 2 * k, because
#           2 * k = (\prod_{i=1}^{k - 2} 1) * 2 * k = (k - 2) * 1 + 2 + k,
#   that is, 2 * k is both a product and a sum of 2, k and (k - 2) ones.
#
#   (iv) This also gives an upper bound for the number r of factors >= 2 in a
#   k-minimal product-sum number, namely:
#           r <= floor(log_2(2 * k))
#   In particular, we can generate all such numbers for k <= N if we take r
#   between 2 and F = floor(log_2(2 * N)) = 1 + floor(log_2(N)).
#
#   (v) Combining the previous points, it follows that we can generate all
#   minimal product-sum numbers by considering each possible number between 2
#   and F of factors >= 2 and, for each such number k of factors, all
#   lists of such factors (b_1, ..., b_r) whose products n do not exceed 2 * N.
#   We then compare n to the previous candidate for a k-minimal product-sum
#   number.

start = time.time()

N = 12_000
# Maximum number of factors >= 2 necessary to generate all minimal-product sum
# numbers involving k factors/summands for all k <= N:
F = int(log(N, 2)) + 1
# Initialize a dictionary to store the minimal product-sum numbers:
minimals = {k: 2 * k for k in range(2, N + 1)}

# Because the solution involves a nested iteration of depth up to 14 (the
# maximum number F of factors involved), we circumvent the use of 'for' loops
# by emulating it through a list of length equal to the depth of the nesting.
# The members of the list are the various counters involved. We also use a
# 'moving head' to store the current position we are dealing with in the list
# and to break out or move into one of the loops as necessary. This makes the
# code more concise and readable.
for number_of_factors in range(2, F + 1):
    # Initialize the list of factors with number_of_factors 2's:
    factors = [2 for _ in range(number_of_factors)]
    # To increment the factors, we use a moving head, beginning from right
    # to left. It is only necessary to search through those lists
    # (b_1, b_2, ..., b_r) for which b_1 <= b_2 <= ... <= b_r.
    completed_loop = False
    while not completed_loop:
        # At each step, set the head to the last position and compute the
        # product n:
        head = number_of_factors - 1
        n = prod(factors)
        if n > 2 * N:
            # If at some point the product n is greater than the bound 2 * N,
            # move the head left, increment the value at this position by 1 and
            # set all factors to its right equal to the new value. Repeat as
            # necessary until the product is <= 2 * N.
            while(prod(factors)) > 2 * N:
                head -= 1
                # This will generate a key-value error (head < 0) if (and only
                # if) the first factor by itself is already greater than 2 * N.
                # This means that we have exhausted all products involving
                # number_of_factors factors. We catch the error before it
                # occurs and increment the number of factors:
                if head == -1:
                    completed_loop = True
                    break
                factors[head] += 1
                for i in range(head + 1, number_of_factors):
                    factors[i] = factors[head]

        else:
            # If the product is a valid candidate, we compare it to the current
            # k-minimal product-sum number and store it in case it is smaller:
            k = n - sum(factors) + number_of_factors
            if k <= N and n < minimals[k]:
                minimals[k] = n
            factors[head] += 1

# Print the answer:
total = sum({n for n in minimals.values()})
print(total)

end = time.time()
print(f"Program runtime: {end - start} seconds")
