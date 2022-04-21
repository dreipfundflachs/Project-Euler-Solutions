#################################
#  PROJECT EULER - PROBLEM 040  #
#################################
import time


# The concatenation of all numbers from 1 to 10**5 into a single string has
# the following number of digits:
#       9 * 1 + 90 * 2 + 900 * 3 + 9000 * 4 + 90_000 * 5
#   =   9 * (1 + 20 + 300 + 4000 + 50_000)
#   =   488_889
# If we further concatenate all numbers from 10**5 = 100_000 to 199_999,
# each of which has 6 digits, we will extend the length of the string by
# 600_000, thus comfortably exceeding the necessary count of 10**6 digits.

start = time.time()

N = 2 * 10**5
D = 6
NUMBER_STRINGS = [str(number) for number in list(range(1, N))]
DIGITS = ''.join(NUMBER_STRINGS)

product = 1
for n in range(0, D + 1):
    index = 10**n - 1
    product *= int(DIGITS[index])

print(product)

end = time.time()
print(f"Program runtime: {end - start} seconds")
