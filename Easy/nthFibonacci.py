def getNthFib(n):
    # Write your code here.
    initalTwoNums = [0, 1]
    counter = 3
    while counter <= n:
        nextFibNum = initalTwoNums[0] + initalTwoNums[1]
        initalTwoNums[0] = initalTwoNums[1]
        initalTwoNums[1] = nextFibNum
        counter += 1
    if n > 1:
        return initalTwoNums[1]
    else:
        return initalTwoNums[0]

