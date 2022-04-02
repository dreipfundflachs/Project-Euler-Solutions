# PROJECT EULER PROBLEM
from math import factorial
import time


start = time.time()
string = str(factorial(100))
digits = [int(d) for d in string]
result = sum(digits)
print(result)

end = time.time()
print(f"Program runtime: {end - start} seconds")
