from __future__ import print_function, division

def rotate_letter(letter, shift):
    if letter.islower():
        start = ord('a')
    elif letter.isupper():
        start = ord('A')
    else:
        return letter
    return chr(start + (ord(letter) - start + shift) % 26)

def rotate_word(word, shift):
    return ''.join(rotate_letter(c, shift) for c in word)

def find_rotate_pairs(word_list):
    rotate_pairs = []
    word_set = set(word_list)
    
    for word in word_list:
        for shift in range(1, 26):
            rotated = rotate_word(word, shift)
            if rotated in word_set:
                rotate_pairs.append((word, rotated))
    
    return rotate_pairs

if __name__ == '__main__':
    with open('/Users/prajaktapohare/Library/CloudStorage/OneDrive-ILStateUniversity/BIS420/Week 11/words.txt') as f:
        word_list = [line.strip() for line in f]
    
    pairs = find_rotate_pairs(word_list)
    for pair in pairs:
        print(pair)