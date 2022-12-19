def firstNonRepeatingCharacter(string):
    # Write your code here.
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    for idx, char in enumerate(string):
        if char_freq[char] == 1:
            return idx

    return -1
