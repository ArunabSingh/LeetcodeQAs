def firstDuplicateValue(array):
    # Write your code here.
    # The items in the array are from 1 to n.
    # Allowed to mutate the array.

    for num in array:
        mapped_idx = abs(num) - 1
        if array[mapped_idx] < 0:
            return abs(num)
        array[mapped_idx] *= -1
    return -1
