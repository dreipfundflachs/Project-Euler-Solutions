#################################
#  PROJECT EULER - PROBLEM 001  #
#################################
import time


start = time.time()

N: int = 1000

answer: int = 0

for n in range(1, N):
    if n % 3 == 0 or n % 5 == 0:
        answer += n

print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
