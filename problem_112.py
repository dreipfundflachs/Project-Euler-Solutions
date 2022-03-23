# PROJECT EULER PROBLEM 112
import time

# DEFINE FUNCTION TO COMPUTE PROPORTION OF BOUNCY NUMBERS UP TO N GIVEN THE
# LIST BELOW OF ALL NON-BOUNCY NUMBERS

start = time.time()
increasing = []
decreasing = []
constant = [str(k) for k in range(1, 10)]
constant += [str(k) + str(k) for k in range(1, 10)]


for i in range(1, 10):
    for j in range(i + 1, 10):
        s = str(i) + str(j)
        increasing.append(s)

print(increasing)
print(constant)
both = increasing + constant
ls_100 = [str(k) for k in range(1, 100)]
decreasing = list(set(ls_100).difference(both))
decreasing.sort()
print(decreasing)

curr_decreasing = decreasing
curr_increasing = increasing
curr_constant = constant[9:]

new_increasing = []
new_constant = []
new_decreasing = []

for r in range(3, 8):

    for x in curr_increasing:
        m = int(x[-1])
        for k in range(m, 10):
            y = x + str(k)
            new_increasing.append(y)

    new_decreasing = []
    for x in curr_decreasing:
        m = int(x[-1])
        for k in range(0, m + 1):
            y = x + str(k)
            new_decreasing.append(y)

    for x in curr_constant:
        m = int(x[-1])
        y = x + str(m)
        new_constant.append(y)
        for k in range(0, m):
            y = x + str(k)
            new_decreasing.append(y)
        for k in range(m + 1, 10):
            y = x + str(k)
            new_increasing.append(y)

    increasing += new_increasing
    decreasing += new_decreasing
    constant += new_constant
    curr_constant = new_constant
    new_constant = []
    curr_increasing = new_increasing
    new_increasing = []
    curr_decreasing = new_decreasing
    new_decreasing = []
    print(increasing)
    print(decreasing)
    print(constant)

    bouncy = 10**r - len(increasing) - len(decreasing) - len(constant)
    prop = bouncy / (10**r)
    print(prop)


end = time.time()
print(f"Program runtime is: {end - start} seconds")
