from __future__ import print_function, division

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))
    t.sort()
    for x in t:
        print(x)


def filter_length(d, n):
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('/Users/prajaktapohare/Library/CloudStorage/OneDrive-ILStateUniversity/BIS420/Week 12/words.txt')
    print_anagram_sets_in_order(anagram_map)
    eight_letters = filter_length(anagram_map, 8)
    print_anagram_sets_in_order(eight_letters)
