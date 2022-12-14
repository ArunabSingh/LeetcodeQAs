def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()  # [2, 3, 5, 5, 9]

    if fastest:
        blueShirtSpeeds.sort(reverse=True)  # [1, 2, 3, 6, 7] # return 32
    else:
        blueShirtSpeeds.sort(reverse=False)  # [7, 6, 3, 2, 1] # return 25
    total_speed = 0

    for idx in range(0, len(redShirtSpeeds)):
        total_speed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])

    return total_speed

