#################################
#  PROJECT EULER - PROBLEM 030  #
#################################
import time


start = time.time()
# A number of 6 digits which is a sum of the fifth powers of its digits must
# be less than or equal to N, where:
N = 6 * 9**5
# Numbers having d digits where d >= 7 cannot be written as the sum of the
# fifth powers of their digits because 10**(d - 1) > d * 9**5 in this case.

special_numbers = []

for number in range(2, N + 1):
    number_string = str(number)
    sum_of_powers_of_digits = 0
    for digit in number_string:
        sum_of_powers_of_digits += int(digit)**5
    if sum_of_powers_of_digits == number:
        special_numbers.append(number)

print(sum(special_numbers))

end = time.time()
print(f"Program runtime: {end - start} seconds")
