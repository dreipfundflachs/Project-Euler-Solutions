# PROJECT EULER PROBLEM 097
import time


def get_digits(n, count):
    """ Returns a list of the first (count) digits of a number (n)."""
    digits = []
    for k in range(count):
        r = n % 10
        n = n // 10
        digits.append(r)

    return digits


# A direct approach works
start = time.time()
n = 28433 * (2**7830457) + 1
string = [str(k) for k in get_digits(n, 10)]
answer = int(''.join(string[::-1]))
print(answer)
print(get_digits(123456789, 4))

end = time.time()
print(f"Program runtime is: {end - start} seconds")
