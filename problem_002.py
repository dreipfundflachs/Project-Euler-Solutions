#################################
#  PROJECT EULER - PROBLEM 002  #
#################################

# First solution, without observing that the even terms occur with period 3.
import time


start = time.time()

N = 4 * 10**6

previous = 1
current = 2
answer = 0

while current <= N:
    if current % 2 == 0:
        answer += current
    current, previous = current + previous, current

print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
