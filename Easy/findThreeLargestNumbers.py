def findThreeLargestNumbers(array):
    # Write your code here.
    largest = []
    for idx in range(0, 3):
        largest.append(array[idx])

    largest.sort()

    for idx in range(3, len(array)):
        largest = insertNumber(array[idx], largest)

    return largest


def insertNumber(x, array):
    # insert x into the sorted array of length 3
    if x <= array[0]:
        return array
    if x <= array[1]:
        array[0] = x
        return array
    if x <= array[2]:
        array[0] = array[1]
        array[1] = x
        return array
    array[0] = array[1]
    array[1] = array[2]
    array[2] = x
    return array
