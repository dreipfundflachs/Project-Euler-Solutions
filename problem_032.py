#################################
#  PROJECT EULER - PROBLEM 032  #
#################################
import time


start = time.time()

N = 10**4

pandigitals = []
for m in range(1, N):
    for n in range(m, N):
        product = m * n
        string = str(m) + str(n) + str(product)
        if len(string) > 9:
            break
        elif len(set(string)) == 9 and '0' not in string:
            pandigitals.append(product)
            print(f"{m} x {n} = {product}")

print('\nAnswer:', sum(set(pandigitals)))

end = time.time()
print(f"Program runtime: {end - start} seconds")
