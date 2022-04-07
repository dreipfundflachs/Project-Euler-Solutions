#################################
#  PROJECT EULER - PROBLEM 094  #
#################################
import time
# Let s denote the length of the congruent sides, b the length of the base and
# h the length of the height of the triangle. Then we seek those integral
# values of s for which b = s +- 1 and the area = b * h / 2 is also an integer.

# Since b = s +- 1, we have s**2 = h**2 + (b / 2)**2 = h**2 + (s +- 1)**2 / 4,
# so that 3 * s**2 - 2 * s - 1 = 4 * h**2, or still,
# (1) [(3s -+ 1) / 2]**2 - 3 * h**2 = 1.
# This is a particular case of Pell's equation x**2 - N * y**2 = 1, with N = 3.
# It is known that its solutions are related to the convergents of the
# continued fraction of the square root of N (= 3 in our case). See
# https://en.wikipedia.org/wiki/Pell's_equation. More precisely, the so-called
# fundamental solution is (x_0, y_0) where x_0 / y_0 is the first convergent
# (in our case, x_0 = 2 and y_0 = 1). All other solutions (x_k, y_k) are
# related to the fundamental solutions. They are given recursively by:
# (2) x_k = x_0 * x_{k - 1} + N * y_0 * y_{k - 1}
# (3) y_k = x_0 * y_{k - 1} + y_0 * x_{k - 1}
# The idea is to use these two formulas to compute the successive solutions to
# the equation, find the associated values of s = (2 * x +- 1) / 3, h = y,
# b = s +- 1 = 2 * (x +- 2) / 3 and the area = b * h / 2 = (x +- 2) * y / 3. We
# require s and area to be positive integers. To avoid checking this directly
# through the function "int" when the numbers involved are possibly quite
# large, which could lead to overflow errors, we instead check whether 3 * s
# and 3 * area are both divisible by 3. We repeat these computations
# for increasing k until the perimiter exceeds one billion, updating our answer
# everytime a solution is found.

start = time.time()

C = 10**9

# Fundamental solution:
x = [2]
y = [1]

# Initialize the smaller perimeter, which will be used in the while condition,
# the answer and k. 'm' and 'p' are abbreviations for 'plus' and 'minus'.
perimeter_m = 0
answer = 0
k = 0
while perimeter_m <= C:
    three_side_p = 2 * x[k] + 1
    three_side_m = 2 * x[k] - 1
    three_area_p = (x[k] + 2) * y[k]
    three_area_m = (x[k] - 2) * y[k]
    perimeter_p = 2 * x[k] + 2
    perimeter_m = 2 * x[k] - 2
    if (three_side_p % 3) == 0 and (three_area_p % 3) == 0\
            and 0 < perimeter_p <= C and 0 < three_area_p:
        answer += perimeter_p
    if (three_side_m % 3) == 0 and (three_area_m % 3) == 0\
            and 0 < perimeter_m <= C and 0 < three_area_m:
        answer += perimeter_m
    k += 1
    x.append(x[0] * x[k - 1] + 3 * y[0] * y[k - 1])
    y.append(x[0] * y[k - 1] + y[0] * x[k - 1])

print(answer)
end = time.time()
print(f"Program runtime: {end - start} seconds")
