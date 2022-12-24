def arrayOfProducts(array):
    # Write your code here.
    output = [1 for _ in array]

    left_running_prod = 1
    for idx in range(0, len(array)):
        output[idx] = left_running_prod
        left_running_prod *= array[idx]

    right_running_prod = 1
    for idx in reversed(range(len(array))):
        output[idx] *= right_running_prod
        right_running_prod *= array[idx]

    return output
