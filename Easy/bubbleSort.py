def bubbleSort(array):
    # Write your code here.
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                swap(i, j, array)
    return array


def swap(i, j, array):
    temp = array[j]
    array[j] = array[i]
    array[i] = temp