#################################
#  PROJECT EULER - PROBLEM 138  #
#################################
import time
from math import gcd

L = 1
count = 0
answer = 0
N = 10**6

L = 1
# b = (+4 + 2 * isqrt(5 * L**2 - 1)) / 5
# print(L, b)
for n in range(1, N):
    for m in range(n + 1, N):
        if (m + n) % 2 == 1 and gcd(m, n) == 1:
            u = m**2 - n**2
            v = 2 * m * n
        if abs(u - 2 * v) == 1:
            count += 1
            L = m**2 + n**2
            print(2 * v, L)

# while True:
#     delta = 5 * L**2 - 1
#     root = isqrt(delta)
#     if root**2 == delta:
#         if (-4 + 2 * root) % 5 == 0:
#             b = (-4 + 2 * root) // 5
#             answer += L
#             count += 1
#             print(L, b, "minus")
#             if count == 5:
#                 print(answer)
#         elif (4 + 2 * root) % 5 == 0:
#             b = (4 + 2 * root) // 5
#             answer += L
#             count += 1
#             print(L, b)
#             if count == 5:
#                 print(answer)
#                 break
#     L += 1

start = time.time()

end = time.time()
print(f"Program runtime: {end - start} seconds")
