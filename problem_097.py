#################################
#  PROJECT EULER - PROBLEM 097  #
#################################
import time


def get_digits(n: int, count: int) -> list[int]:
    """ Returns a list of the first (count) digits of a number (n)."""
    digits = []
    for k in range(count):
        r = n % 10
        n = n // 10
        digits.append(r)
    return digits


# A direct approach works
start = time.time()

N = 28433 * (2**7830457) + 1

string = [str(k) for k in get_digits(N, 10)]
answer = int(''.join(string[::-1]))

print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
