def isValidSubsequence(array, sequence):
    # Write your code here.
    if len(sequence) > len(array):
        return False

    pointer = 0
    for num in array:  # [5, 1, 22, 25, 6, -1, 8, 10]
        if pointer < len(sequence):
            if num == sequence[pointer]:  # [22, 25, 6]
                pointer += 1

    return pointer == len(sequence)

