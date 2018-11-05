
from poker import Deck
from poker import Hand
from poker import results

result_dict = {}
for result in results:
    result_dict[result] = 0

# for i in range(10000):
#     new_deck = Deck()
#     new_deck.shuffle()
#     for j in range(10):
#         hand = Hand(new_deck)
#         if hand.is_full_house():
#             print("Full House: ", hand)


for i in range(100000):
#while result_dict[results[0]] == 0:

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

for i in result_dict:
    print(i, " ", result_dict[i]*100/total, "%", end=" ")

