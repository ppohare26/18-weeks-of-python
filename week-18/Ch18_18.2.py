class Card:
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)

    def __str__(self):
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in range(4)
                      for rank in range(1, 14)]

    def sort(self):
        self.cards.sort()

    def __str__(self):
        return '\n'.join(str(card) for card in self.cards)

deck = Deck()
import random
random.shuffle(deck.cards)

print("Shuffled Deck:")
print(deck)

deck.sort()
print("\nSorted Deck:")
print(deck)
