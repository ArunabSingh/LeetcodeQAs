def generateDocument(characters, document):
    # Write your code here.
    chars = {}

    for char in characters:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for char in document:
        if char in chars:
            if chars[char] == 1:
                chars.pop(char)
            else:
                chars[char] -= 1
        else:
            return False
    return True
