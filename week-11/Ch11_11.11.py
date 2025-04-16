from __future__ import print_function, division

from pronounce import read_dictionary

def make_word_dict():
    d = {}
    with open('/Users/prajaktapohare/Library/CloudStorage/OneDrive-ILStateUniversity/BIS420/Week 11/words.txt') as fin:
        for line in fin:
            word = line.strip().lower()
            d[word] = word
    return d

def homophones(a, b, phonetic):
  
    return a in phonetic and b in phonetic and phonetic[a] == phonetic[b]

def check_word(word, word_dict, phonetic):
   
    word1 = word[1:]
    word2 = word[0] + word[2:]

    return (word1 in word_dict and word2 in word_dict and 
            homophones(word, word1, phonetic) and 
            homophones(word, word2, phonetic))

if __name__ == '__main__':
    phonetic = read_dictionary()
    word_dict = make_word_dict()
    
    if not word_dict:
        print("No words to process. Check if words.txt has content.")

    for word in word_dict:
        if check_word(word, word_dict, phonetic):
            print(word, word[1:], word[0] + word[2:])
