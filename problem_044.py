# PROJECT EULER PROBLEM 044
import time

start = time.time()
pentagonals = []
for n in range(1, 3000):
    pent = n * (3*n - 1) // 2
    pentagonals.append(pent)

set_of_pentagonals = set(pentagonals)
m = len(pentagonals)
print(pentagonals)
for i in range(1, m):
    for j in range(i + 1, m):
        s = pentagonals[i] + pentagonals[j]
        d = pentagonals[j] - pentagonals[i]
        if s in set_of_pentagonals and d in set_of_pentagonals:
            message = f"Pentagonals {pentagonals[i]} and {pentagonals[j]}"
            message += f"\nhave sum equal to {s} and difference equal to {d}."
            print(message.strip())

end = time.time()
print(f"Program runtime: {end - start} seconds")
