#################################
#  PROJECT EULER - PROBLEM 048  #
#################################
import time


start = time.time()

N = 1000
M = 10**10  # We are interested in the sum of the series modulo M.

answer = 0
for n in range(1, N + 1):
    answer = (answer + n**n % M) % M

print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
