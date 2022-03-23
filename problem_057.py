# PROJECT EULER PROBLEM 057
import time
from project_euler import number_of_digits

start = time.time()
p = [3]
q = [2]
count = 0

# The recursive formula for the numerator and denominator are as follows:
for k in range(1, 10**3):
    newp = p[k - 1] + 2 * q[k - 1]
    newq = p[k - 1] + q[k - 1]
    p.append(newp)
    q.append(newq)
    if number_of_digits(newp) > number_of_digits(newq):
        count += 1

end = time.time()
print(f"Program runtime is: {end - start} seconds")
