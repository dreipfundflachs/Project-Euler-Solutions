#################################
#  PROJECT EULER - PROBLEM 031  #
#################################
import time


start = time.time()

TARGET = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

# Using dynamic programming:
ways = [1] + [0] * 200
for coin in COINS:
    for k in range(coin, TARGET + 1):
        ways[k] += ways[k - coin]

print(ways[TARGET])

end = time.time()
print(f"Program runtime: {end - start} seconds")
