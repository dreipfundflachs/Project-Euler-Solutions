def binary_search(target: int, numbers: list[int]) -> int:
    """ Given a _sorted_ list of integers 'numbers', uses a binary search to
    find the 'target' in it. Returns an index i such that numbers[i] = target
    (not necessarily the first one) or (-1) if target is not in numbers. """
    first = 0
    last = len(numbers) - 1
    middle = 0

    while first <= last:
        middle = (first + last) // 2
        if numbers[middle] == target:
            return middle
        elif target < numbers[middle]:
            last = middle - 1
        else:
            first = middle + 1

    return -1


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for n in range(-1, 14):
    if binary_search(n, lst) != n:
        print(n)
