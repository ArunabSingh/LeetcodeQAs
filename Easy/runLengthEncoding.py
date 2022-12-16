def runLengthEncoding(string):
    # Write your code here.
    encodedString = ""
    currentCharLength = 1

    for idx in range(1, len(string)):
        if string[idx] != string[idx - 1] or currentCharLength == 9:
            encodedString += str(currentCharLength)
            encodedString += string[idx - 1]
            currentCharLength = 0
        currentCharLength += 1

    encodedString += str(currentCharLength)
    encodedString += string[len(string) - 1]

    return encodedString


