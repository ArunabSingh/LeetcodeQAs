def twoNumberSum(array, targetSum):
    # Write your code here.
    if len(array) == 1:
        return []

    complimentSet = set()

    for num in array:
        x = num
        y = targetSum - x
        if x in complimentSet:
            return [x, y]
        else:
            complimentSet.add(y)

    return []


