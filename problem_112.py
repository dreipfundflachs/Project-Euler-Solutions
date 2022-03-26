# PROJECT EULER PROBLEM 112
import time

start = time.time()

# The value of N below was set after finding the answer to, decrease runtime.
N = 16 * 10**5

# Begin by initializing dictionaries to flag all decreasing and increasing
# numbers. Note that a number may be both increasing and decreasing
# simultaneously if its digits form a constant sequence, but this will be
# irrelevant below.  We use strings instead of integers as keys in order to
# consider cases such as '01' or '00' as valid.
decreasing = {str(n): False for n in range(10, N + 1)}
increasing = {str(n): False for n in range(10, N + 1)}

# Flag all increasing and all decreasing strings between '00' and '99'.
for a in range(0, 10):
    for b in range(a, 10):
        increasing[str(a) + str(b)] = True
        decreasing[str(b) + str(a)] = True

bouncy = 0
# To identify new increasing or decreasing numbers n, we compare its trailing
# digit to its next-to-last digit, and also verify whether the substring
# obtained by discarding the trailing digit is increasing or decreasing.
for n in range(100, N + 1):
    s = str(n)
    trailing_digit = int(s[-1])
    next_to_last_digit = int(s[-2])
    if trailing_digit <= next_to_last_digit and decreasing[s[:-1]]:
        decreasing[str(n)] = True
    if trailing_digit >= next_to_last_digit and increasing[s[:-1]]:
        increasing[str(n)] = True
    # If n is neither increasing nor decreasing, it must be bouncy.
    if not (increasing[str(n)] or decreasing[str(n)]):
        bouncy += 1
        proportion = bouncy / n
        if proportion >= 0.99:
            print(n, proportion)
            break

end = time.time()
print(f"Program runtime is: {end - start} seconds")
