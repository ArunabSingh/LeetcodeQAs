def mergeOverlappingIntervals(intervals):
    # Write your code here.
    # Overlapping happens when the interval[1] is greater or equal to the interval[0] of the next interval
    output = []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    print(sorted_intervals)
    # For every interval in the array,
    # We compare the current interval's [1] to next interval's [0]
    # If they overlap, we change the current interval's [1] value to match the next interval's [1] value

    idx = 0
    while idx < len(sorted_intervals):
        next_idx = idx + 1
        while next_idx < len(intervals) and sorted_intervals[idx][1] >= sorted_intervals[next_idx][0]:
            sorted_intervals[idx][1] = max(sorted_intervals[idx][1], sorted_intervals[next_idx][1])
            next_idx += 1
        output.append(sorted_intervals[idx])
        if next_idx > idx + 1:
            idx = next_idx
        else:
            idx += 1
    return output

