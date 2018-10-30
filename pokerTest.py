
from poker import Deck
from poker import Hand

#new_deck = Deck()
#new_deck.shuffle()
#print(new_deck)
for i in range(1000000):
    new_deck = Deck()
    new_deck.shuffle()
    hand = Hand(new_deck)
    #print(hand)
    if hand.is_royal_flush():
        print("Royal Flush *****", hand)
        print(hand.high_card())
