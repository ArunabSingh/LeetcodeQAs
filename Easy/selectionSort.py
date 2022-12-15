def selectionSort(array):
    # Write your code here.
    for i in range(0, len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array
