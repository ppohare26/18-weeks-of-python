def consecutivedl(word):
    count = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            i += 2
        else:
            count = 0
            i += 1
        if count == 3:
            return True
    return False

def find(word_list):
    for word in word_list:
        if consecutivedl(word):
            return word
    return None

# Example word list
word_list = ["committee", "Mississippi", "bookkeeper", "bookkeeping"]

result = find(word_list)
print(f"The word with three consecutive double letters is: {result}")