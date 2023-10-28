import collections

Card = collections.namedtuple('card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, positon):
        return self._cards[positon]

    suit_value = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
    
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_value) + suit_value[card.suits]
        

beer_card = Card('7','diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))
print(deck)
#print(deck[0])
#print(deck[::])
for card in deck:
    print(card)
for card in reversed(deck): #we can iterate over reversed deck
    print(card)

print(Card('A','hearts') in deck)
