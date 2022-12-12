def sortedSquaredArray(array):
    # Write your code here.
    sqArray = [0 for _ in array]
    smIdx = 0
    largeIdx = len(array) - 1
    for idx in reversed(range(len(array))):
        left = array[smIdx]  # smallest Value
        right = array[largeIdx]  # Largest Value
        if abs(left) > abs(right):
            sqArray[idx] = left * left
            smIdx += 1
        else:
            sqArray[idx] = right * right
            largeIdx -= 1
    return sqArray
