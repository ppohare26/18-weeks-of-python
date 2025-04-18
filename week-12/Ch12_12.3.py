from __future__ import print_function, division


def most_frequent(text):
    letter_count = get_frequency_dict(text)

    freq_pairs = []
    for char, count in letter_count.items():
        freq_pairs.append((count, char))

    freq_pairs.sort(reverse=True)

    sorted_letters = []
    for count, char in freq_pairs:
        sorted_letters.append(char)

    return sorted_letters


def get_frequency_dict(text):
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict


def load_text(filepath):
    return open(filepath).read()


if __name__ == '__main__':
    content = load_text('/Users/prajaktapohare/Library/CloudStorage/OneDrive-ILStateUniversity/BIS420/Week 12/emma.txt')
    result = most_frequent(content)
    for letter in result:
        print(letter)
