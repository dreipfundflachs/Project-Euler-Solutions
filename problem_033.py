#################################
#  PROJECT EULER - PROBLEM 033  #
#################################
import time
from fractions import Fraction


def is_cancellable(num_string: str, den_string: str) -> bool:
    """ Determines if the fraction int(num_string) / int(den_string)
    is 'cancellable' in the sense of the problem statement. """
    num = int(num_string)
    den = int(den_string)

    if num >= den:
        return False
    if num_string[0] == den_string[0] and\
            int(num_string[1]) / int(den_string[1]) == num / den:
        return True
    elif num_string[0] == den_string[1] and\
            int(num_string[1]) / int(den_string[0]) == num / den:
        return True
    elif num_string[1] == den_string[0] and\
            int(num_string[0]) / int(den_string[1]) == num / den:
        return True
    elif num_string[1] == den_string[1] and\
            int(num_string[0]) / int(den_string[0]) == num / den:
        return True


start = time.time()

NUMBER_STRINGS = [str(number) for number in range(10, 100)
                  if '0' not in str(number)]

special_pairs = []
for numerator_str in NUMBER_STRINGS:
    for denominator_str in NUMBER_STRINGS:
        if is_cancellable(numerator_str, denominator_str):
            special_pairs.append((int(numerator_str), int(denominator_str)))

num_product = 1
den_product = 1
for (num, den) in special_pairs:
    num_product *= num
    den_product *= den

print((Fraction(num_product, den_product)).denominator)

end = time.time()
print(f"Program runtime: {end - start} seconds")
