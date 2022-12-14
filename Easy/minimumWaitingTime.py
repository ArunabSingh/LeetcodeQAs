def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()

    total_wt = 0
    for idx in range(0, len(queries)):
        queries_left = len(queries) - (idx + 1)
        total_wt += queries[idx] * queries_left

    return total_wt


