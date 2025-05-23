

from __future__ import print_function, division

import random


class Card:
  
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
       
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __eq__(self, other):
      
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
      
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
  
    
    def __init__(self):
       
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
 
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        
        self.cards.append(card)

    def remove_card(self, card):
       
        self.cards.remove(card)

    def pop_card(self, i=-1):
       
        return self.cards.pop(i)

    def shuffle(self):
       
        random.shuffle(self.cards)

    def sort(self):
    
        self.cards.sort()

    def move_cards(self, hand, num):

        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)