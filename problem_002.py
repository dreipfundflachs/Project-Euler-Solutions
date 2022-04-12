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
k = 2

while current <= N:
    if current % 2 == 0:
        answer += current

    current, previous = current + previous, current
# Alternatively:
#     new = current + previous
#     previous = current
#     current = new

print(answer)

end = time.time()

print(f"Program runtime: {end - start} seconds")


###########################################################################


# Second (faster) solution, using that the even terms occur with period 3.

start = time.time()

N = 4 * 10**6

previous = 1
current = 2
answer = 0
k = 2

while current <= N:
    if (k - 2) % 3 == 0:
        answer += current

    k += 1
    current, previous = current + previous, current
#     new = current + previous
#     previous = current
#     current = new

print(answer)
end = time.time()

print(f"Program runtime: {end - start} seconds")
