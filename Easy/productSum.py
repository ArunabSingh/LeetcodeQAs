# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    # Write your code here.
    product_sum = 0
    for item in array:
        if type(item) is int:
            product_sum += item
        else:
            product_sum += productSum(item, depth+1)
    return product_sum * depth