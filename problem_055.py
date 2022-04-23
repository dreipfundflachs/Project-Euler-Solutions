#################################
#  PROJECT EULER - PROBLEM 055  #
#################################
import time


def reverse_add(n):
    """ Returns the sum of n with number obtained
    by reversing the digits of n.  """
    s = str(n)
    m = int(s[::-1])
    return(m + n)


def is_palindromic(n):
    """ Checks if the given number is palindromic. """
    s = str(n)
    return (s == s[::-1])


start = time.time()

# Initialize a dictionary to hold all Lychrel numbers and another to hold all
# numbers which have been seen before.
lychrels = {}  # lychrels[k] = T or F according as k is Lychrel or not.
seen = {}  # seen[k] = T or F according as k has already appeared or not.
N = 10**4

# For each number in the range, follow its chain to determine whether it is
# Lychrel.
for n in range(0, N):
    count = 0
    curr = [n]
    m = reverse_add(n)
    curr.append(m)

    # If we reach a number which has already been seen, which is palindromic or
    # if the chain has length > 50, then we can stop following it.
    while seen.get(m) is None and count < 50 and not is_palindromic(m):
        m = reverse_add(m)
        curr.append(m)
        count += 1
    is_lychrel = lychrels.get(m)

    # Every number in the chain has now been seen.
    for k in curr:
        seen[k] = True
        # Sum up our findings.
        if is_lychrel:
            lychrels[k] = True
        elif not is_lychrel:
            lychrels[k] = False
        elif is_palindromic(m):
            lychrels[k] = False
        elif count == 50:
            lychrels[k] = True

# Compute the number of Lychrel numbers under N.
number_of_lychrels = 0
for k in range(0, N):
    if lychrels[k]:
        number_of_lychrels += 1
print(number_of_lychrels)

end = time.time()
print(f"Program runtime: {end - start} seconds")
