def isPalindrome(string):
    # Write your code here.
    start = 0
    end = len(string) - 1
    middle = len(string) // 2

    for _ in range(0, middle):
        if string[start] != string[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

