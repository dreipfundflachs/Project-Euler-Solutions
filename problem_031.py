# PROJECT EULER - PROBLEM 31
import time


start = time.time()
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*200
for coin in coins:
    for k in range(coin, target + 1):
        ways[k] += ways[k-coin]

print(ways[target])

end = time.time()
print(f"Program runtime: {end - start} seconds")
