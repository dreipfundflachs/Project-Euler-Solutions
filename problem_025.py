#################################
#  PROJECT EULER - PROBLEM 025  #
#################################
import time


start = time.time()

N = 10**3

fibs = [1, 1]
n = 3
while True:
    current_fib = fibs[-1] + fibs[-2]
    fibs.append(current_fib)
    if len(str(current_fib)) >= N:
        print(n)
        break
    n += 1

end = time.time()
print(f"Program runtime: {end - start} seconds")
