#################################
#  PROJECT EULER - PROBLEM 020  #
#################################
import time
from math import factorial


start = time.time()

N = 100

factorial_string = str(factorial(N))
digits = [int(d) for d in factorial_string]
sum_of_digits = sum(digits)

print(sum_of_digits)

end = time.time()
print(f"Program runtime: {end - start} seconds")
