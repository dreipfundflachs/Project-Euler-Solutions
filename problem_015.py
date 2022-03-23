# PROJECT EULER PROBLEM
import time
from math import factorial


start = time.time()

a = factorial(40)
b = factorial(20)
result = int(a / (b**2))

print(result)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
