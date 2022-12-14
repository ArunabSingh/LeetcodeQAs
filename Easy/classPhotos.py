def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    biggerOne = ""
    if redShirtHeights[0] > blueShirtHeights[0]:
        biggerOne = "red"
    elif redShirtHeights[0] < blueShirtHeights[0]:
        biggerOne = "blue"
    else:
        return False

    if biggerOne == "red":
        for idx in range(0, len(redShirtHeights)):
            if redShirtHeights[idx] <= blueShirtHeights[idx]:
                return False
    else:
        for idx in range(0, len(blueShirtHeights)):
            if redShirtHeights[idx] >= blueShirtHeights[idx]:
                return False
    return True

