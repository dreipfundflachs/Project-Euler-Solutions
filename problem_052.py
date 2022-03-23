# PROJECT EULER PROBLEM 052
import time


start = time.time()

n = 1
active = True
while active:
    string = str(n)
# No need to test those number who first digit is not equal to 1. This will be
# the case for the first time for a number such as 20, 200, 2000, ..., and then
# we can skip to 10**d where d is the number of its digits.
    if string[0] != '1':
        d = len(string)
        n = 10**d - 1
    else:
        s = set(string)
        if (set(str(2 * n)) == s and set(str(3 * n)) == s and
                set(str(4 * n)) == s and set(str(5 * n)) == s and
                set(str(6 * n)) == s and len(str(n)) == len(str(6 * n))):
            active = False
            print(n, 2*n, 3*n, 4*n, 5*n, 6*n)
    n += 1

end = time.time()
print(f"Program runtime is: {end - start} seconds")
