def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    smallest_diff = float("inf")
    smallest_pair = []

    first_ptr = 0
    second_ptr = 0

    while first_ptr < len(arrayOne) and second_ptr < len(arrayTwo):
        current_diff = abs(arrayOne[first_ptr] - arrayTwo[second_ptr])
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            smallest_pair.clear()
            smallest_pair.append(arrayOne[first_ptr])
            smallest_pair.append(arrayTwo[second_ptr])
        if arrayOne[first_ptr] < arrayTwo[second_ptr]:
            first_ptr += 1
        else:
            second_ptr += 1

    return smallest_pair
