# PROJECT EULER - PROBLEM 092
import time


def sum_of_squares(n):
    "Calculates the sum of the squares of all digits of an integer n."
    sq_sum = 0
    while n != 0:
        r = n % 10
        sq_sum += r**2
        n = n // 10
    return sq_sum


start = time.time()

# Calculate the maximum possible sum of squares (r)
r = 7*81

# Initialize the sets of all numbers which are sum of squares and whose chains
# end in 1 or 89, respectively
ends = [0]*(r+1)
ends[1] = 1
ends[89] = 89

# Determine the two sets described above
for n in range(1, r + 1):
    active = True
    curr = [n]
    m = n
    while active:
        if ends[m] == 89:
            for k in curr:
                ends[k] = 89
            active = False
        elif ends[m] == 1:
            for k in curr:
                ends[k] = 1
            active = False
        else:
            m = sum_of_squares(m)
            curr.append(m)

# Since all possible sums of squares have already appeared, for n > r, any
# chain will only advance one step before encountering an already seen element
# count_1 = sum(value == 1 for value in ends.values())
count_89 = ends.count(89)

for n in range(r + 1, 10**7):
    m = sum_of_squares(n)
    if ends[m] == 89:
        count_89 += 1
#     else:
#         count_1 += 1

print(count_89)

end = time.time()
print(f"Program runtime: {end - start} seconds")
