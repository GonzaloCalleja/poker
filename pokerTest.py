
from poker import Deck
from poker import Hand
from poker import results

result_dict = {}
for result in results:
    result_dict[result] = 0


for i in range(10000):

    new_deck = Deck()
    new_deck.shuffle()
    # 10 hands per deck, right?
#for j in range(10):
    hand = Hand(new_deck)
    result_dict[hand.check_ranking()] += 1

print(result_dict)

# checking that all hands get assigned a result
total = 0
for i in result_dict:
    total += result_dict[i]

print(total)
new_deck = Deck()
print(len(new_deck.cards))
