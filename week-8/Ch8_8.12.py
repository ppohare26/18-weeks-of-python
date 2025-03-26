def rotate_word(s, n):
    result = ''
    for char in s:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            rotated_char = chr(start + (ord(char) - start + n) % 26)
            result += rotated_char
        else:
            result += char
    return result


print(rotate_word("cheer", 7)) 
print(rotate_word("melon", -10)) 