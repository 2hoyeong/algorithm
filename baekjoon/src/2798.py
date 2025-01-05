from itertools import combinations

N, M = map(int, input().split())
cards = map(int, input().split())

cards_combi = list(combinations(cards, 3))
cards_sum = []
for card in cards_combi:
    card_sum = sum(card)
    if card_sum <= M:
        cards_sum.append(card_sum)

print(max(cards_sum))
