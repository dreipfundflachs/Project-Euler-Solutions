# PROJECT EULER PROBLEM 4

def palindrome(n):
    """ Return the largest palindromic number that is the product
    of two numbers having at most n digits each
    """
    products = [
        str(a*b)
        for a in range(10**n, 1, -1)
        for b in range(10**n, 1, -1)
    ]
    palindromic = []
    for number in products:
        rebmun = number[::-1]
        if number == rebmun:
            palindromic.append(int(number))
    return palindromic


print(palindrome(3))
print(max(palindrome(3)))


# products = [
#     str(a*b)
#     for a in range(1, 10**1, -1)
#     for b in range(1, 10**1, -1)
# ]
#
# print(products)
# palindromic = 9
# for number in products:
#     rebmun = number[::-1]
#     print(f"{number} --- {rebmun}")
#     if number == rebmun:
#         print("True")
#         palindromic = int(number)
#         break
#     else:
#         print("False")
