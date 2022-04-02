# PROJECT EULER - PROBLEM 026
import time


def int_division(r, d, prec):
    """ Given integers r < d, computes the decimal part of r/d up to the
    'prec'-th digit of its decimal part or until there is a recurring cycle.
    The function does not determine the cycle. 'x' indicates a recurring cycle
    from that position on.
    """
    decimals = []
    remainders = [r]
    digit = -1
    count = 0
    while r != 0 and count < prec:
        r *= 10
        while r < d:
            r *= 10
            decimals.append(0)
            count += 1
            remainders.append(r)
        digit = r // d
        decimals.append(digit)
        r = (r % d)
        count += 1
        if r not in remainders:
            remainders.append(r)
        else:
            decimals.append('x')
            break
    return decimals


max_length = 0
max_d = 0
for d in range(2, 1000):
    length = len(int_division(1, d, 1000)) - 1
    if length > max_length:
        max_length = length
        max_d = d

print(int_division(1, 8, 100))
print(max_d)
print(max_length)
start = time.time()
end = time.time()
print(f"Program runtime: {end - start} seconds")
