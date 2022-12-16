def caesarCipherEncryptor(string, key):
    # Write your code here.
    encrypted = ""
    for letter in string:
        new_unicode_value = ord(letter) + key
        while new_unicode_value > ord('z'):
            new_unicode_value -= 26
        new_letter = chr(new_unicode_value)
        encrypted += new_letter

    return encrypted
