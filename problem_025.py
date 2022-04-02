# PROJECT EULER - PROBLEM 025
import time


start = time.time()
fib = [1, 1]
for n in range(3, 10**6):
    current = fib[-1] + fib[-2]
    fib.append(current)
    string = str(current)
    if len(string) > 999:
        print(current)
        print(n)
        break


end = time.time()
print(f"Program runtime: {end - start} seconds")
