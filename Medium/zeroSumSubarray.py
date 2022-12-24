def zeroSumSubarray(nums):
    # Write your code here.
    sums = set()
    sum = 0
    for value in nums:
        sum += value
        if sum in sums:
            return True
        sums.add(sum)

    if 0 in sums:
        return True
    return False
