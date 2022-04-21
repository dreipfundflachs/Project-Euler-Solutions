#################################
#  PROJECT EULER - PROBLEM 038  #
#################################
import time


def is_pandigital(number_string: str) -> bool:
    """ Decides whether a number string is 1-to-9 pandigital. """
    digits_in_number = {int(k) for k in number_string}

    return (len(number_string) == 9 and digits_in_number == set(range(1, 10)))


# We will call the integer that gets multiplied by 1,..., 9 the 'base'.  The
# idea is to loop through all bases having fewer than 5 digits, multiplying
# them by 1, ..., n, ..., 9, and to test whether the concatenation of all of
# these products is pandigital. If it is, update the maxima if necessary.

start = time.time()

N = 10**4

max_base = 1
max_number_of_factors = 1
max_product = 1

for base in range(N):
    concatenation = ''
    for n in range(1, 10):
        concatenation += str(base * n)
        if len(concatenation) > 9:
            break
        elif is_pandigital(concatenation):
            product = int(concatenation)
            if product > max_product:
                max_product = product
                max_base = base
                max_number_of_factors = n
                break

print(max_product)

end = time.time()
print(f"Program runtime: {end - start} seconds")
