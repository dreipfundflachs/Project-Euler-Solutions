#################################
#  PROJECT EULER - PROBLEM 052  #
#################################
import time


start = time.time()

n = 1
found_solution = False
while not found_solution:
    n_string = str(n)
    # No need to test those numbers whose first digit is not equal to 1. This
    # will be the case for the first time for a number such as 20, 200, 2000,
    # ..., and then we can skip to 10**d, where d is the current number of
    # digits under consideration.
    if n_string[0] != '1':
        # The new value of n is 10**d, where d is the number of digits of n.
        n = 10**(len(n_string)) - 1  # A 1 will be added to n below.
    else:
        if set(n_string) == set(str(2 * n)) == set(str(3 * n))\
                == set(str(4 * n)) == set(str(5 * n)) == set(str(6 * n)) and\
                len(str(6 * n)) == len(n_string):
            found_solution = True
            print(n, 2 * n, 3 * n, 4 * n, 5 * n, 6 * n)
    n += 1

end = time.time()
print(f"Program runtime: {end - start} seconds")
