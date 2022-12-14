def binarySearch(array, target):
    # Write your code here.
    return bs_helper(array, target, 0, len(array) - 1)


def bs_helper(array, target, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2

    if target > array[middle]:
        return bs_helper(array, target, middle + 1, end)
    elif target < array[middle]:
        return bs_helper(array, target, start, middle - 1)
    else:
        return middle


