# PROJECT EULER - PROBLEM 16

def sum_of_digits(n):
    """ Returns the sum of all the digits of n """
    sum = 0
    while n > 0:
        last = n % 10
        sum += last
        n = (n - last) // 10
    return sum


print(sum_of_digits(2**1000))
