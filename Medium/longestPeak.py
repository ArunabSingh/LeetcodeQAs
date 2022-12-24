def longestPeak(array):
    # Write your code here.

    highest_peak = 0

    for idx in range(1, len(array) - 1):
        current_peak = array[idx]
        left_idx = idx - 1
        right_idx = idx + 1

        if array[left_idx] < current_peak and array[right_idx] < current_peak:
            peak_length = 3

            while right_idx + 1 <= len(array) - 1 and array[right_idx + 1] < array[right_idx]:
                peak_length += 1
                right_idx += 1
            while left_idx - 1 >= 0 and array[left_idx - 1] < array[left_idx]:
                peak_length += 1
                left_idx -= 1
            if peak_length > highest_peak:
                highest_peak = peak_length

    return highest_peak


