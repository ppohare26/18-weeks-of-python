def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

print(is_anagram("listen", "silent")) 
print(is_anagram("hello", "world")) 