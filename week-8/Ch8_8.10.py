def is_palindrome():
    s = input("Enter a string: ")
    return s == s[::-1]

print(is_palindrome())