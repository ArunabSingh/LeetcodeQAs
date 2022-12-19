def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    results = []

    for idx in range(len(array) - 2):
        left = idx + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[idx] + array[left] + array[right]
            if current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1
            else:
                results.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1
    return results
