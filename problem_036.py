#################################
#  PROJECT EULER - PROBLEM 036  #
#################################
import time


def generate_palindromes(letters: list[str], length: int) -> list[str]:
    """ Returns a list containing all palindromes of the specified length using
    the letters (or strings) in the given list of strings. """
    # Base cases:
    if length <= 0:
        palindromes = []
    elif length == 1:
        palindromes = letters
    elif length == 2:
        palindromes = [string + string for string in letters]
    # General case:
    else:
        palindromes = []
        # Choose an initial/final letter and make a recursive call using
        # (length - 2) to generate the central string.
        for letter in letters:
            for palindrome in generate_palindromes(letters, length - 2):
                new_palindrome = letter + palindrome + letter
                palindromes.append(new_palindrome)
    return palindromes


def generate_palindromic_integers(length: int) -> list[int]:
    """ Returns a list of all integers having at most 'length' digits
    which are palindromic when written in base 10. """
    DIGITS = [str(d) for d in range(0, 10)]

    palindromic_strings = generate_palindromes(DIGITS, length)
    palindromic_integers = [int(string) for string in palindromic_strings
                            if string[0] != '0']
    return palindromic_integers


def is_palindromic_base_2(n: int) -> bool:
    """ Determines whether the positive integer n is palindromic when expressed
    as a binary string. """
    if n <= 0:
        return False
    else:
        binary_string = str(bin(n))[2:]
        return binary_string == binary_string[::-1]


start = time.time()

N = 6  # Maximum number of decimal digits to be considered.

# Generate all palindromic integers in base 10.
palindromics_base_10 = []
for number_of_digits in range(1, N + 1):
    palindromics_base_10 += generate_palindromic_integers(number_of_digits)

# Check if these integers are also palindromic in base 2; if so, append them to
# the list of special numbers.
special_numbers = []
for number in palindromics_base_10:
    if is_palindromic_base_2(number):
        special_numbers.append(number)

print(sum(special_numbers))
end = time.time()
print(f"Program runtime: {end - start} seconds")
