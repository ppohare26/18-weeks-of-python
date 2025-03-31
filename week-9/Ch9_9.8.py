def is_palindrome(s):
    return s == s[::-1]

def find_readings():
    for num in range(100000, 1000000):
        s = str(num)
        if is_palindrome(s[2:]):
            if is_palindrome(str(num + 1)[1:]):
                if is_palindrome(str(num + 2)[1:5]):
                    if is_palindrome(str(num + 3)):
                        print(f"The odometer reading when first looked was: {num}")

find_readings()