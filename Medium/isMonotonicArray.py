def isMonotonic(array):
    # Write your code here.
    if len(array) <= 2:
        return True

    is_dec_monotonic = True
    is_inc_monotonic = True

    for idx in range(0, len(array) - 1):
        current_num = array[idx]
        next_num = array[idx + 1]

        if current_num < next_num:
            is_inc_monotonic = False
        if current_num > next_num:
            is_dec_monotonic = False

    return is_inc_monotonic or is_dec_monotonic

