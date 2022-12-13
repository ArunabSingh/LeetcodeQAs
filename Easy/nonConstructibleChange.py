def nonConstructibleChange(coins):
    # Write your code here.
    if len(coins) == 0:
        return 1

    coins.sort()
    changeCreatable = 0

    for coin in coins:
        if coin > changeCreatable + 1:
            return changeCreatable + 1
        else:
            changeCreatable += coin
    return changeCreatable + 1

