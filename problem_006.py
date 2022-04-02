# PROJECT EULER - PROBLEM 6

# Note first that the difference is simply the sum of 2*a*b for a < b and
# a, b between 1 and n

def difference_of_sums(n):
    """
    Calculates the difference between the square of the sum of 1 through n
    and the sum of the squares of all numbers between 1 and n
    """

    numbers = range(1, n+1, 1)
    products = [2*a*b for a in numbers for b in range(a + 1, n+1, 1)]
    return sum(products)


print(difference_of_sums(100))
