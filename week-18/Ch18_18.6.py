from __future__ import print_function, division

from Card import Hand, Deck


class Hist(dict):
  

    def __init__(self, seq=[]):
       
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
      
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]


class PokerHand(Hand):
   
    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_histograms(self):
      
        self.suits = Hist()
        self.ranks = Hist()
        
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)
 
    def has_highcard(self):
        return len(self.cards)
        
    def check_sets(self, *t):
       
        for need, have in zip(t, self.sets):
            if need > have:
                return False
        return True

    def has_pair(self):
        return self.check_sets(2)
        
    def has_twopair(self):
        return self.check_sets(2, 2)
        
    def has_threekind(self):
        return self.check_sets(3)
        
    def has_fourkind(self):
       
        return self.check_sets(4)

    def has_fullhouse(self):
      
        return self.check_sets(3, 2)

    def has_flush(self):
  
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_straight(self):
   
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)

        return self.in_a_row(ranks, 5)

    def in_a_row(self, ranks, n=5):
     
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == n:
                    return True
            else:
                count = 0
        return False
    
    def has_straightflush(self):
   
        s = set()
        for c in self.cards:
            s.add((c.rank, c.suit))
            if c.rank == 1:
                s.add((14, c.suit))

        for suit in range(4):
            count = 0
            for rank in range(1, 15):
                if (rank, suit) in s:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
        return False
                
    def has_straightflush(self):
      
        d = {}
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)

        for hand in d.values():
            if len(hand.cards) < 5:
                continue            
            hand.make_histograms()
            if hand.has_straight():
                return True
        return False

    def classify(self):
       
        self.make_histograms()

        self.labels = []
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)


class PokerDeck(Deck):
 
    def deal_hands(self, num_cards=5, num_hands=10):
    
        hands = []
        for i in range(num_hands):        
            hand = PokerHand()
            self.move_cards(hand, num_cards)
            hand.classify()
            hands.append(hand)
        return hands


def main():
 
    lhist = Hist()

    n = 10000
    for i in range(n):
        if i % 1000 == 0:
            print(i)
            
        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(7, 7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)
            
    # print the results
    total = 7.0 * n
    print(total, 'hands dealt:')

    for label in PokerHand.all_labels:
        freq = lhist.get(label, 0)
        if freq == 0: 
            continue
        p = total / freq
        print('%s happens one time in %.2f' % (label, p))

        
if __name__ == '__main__':
    main()
