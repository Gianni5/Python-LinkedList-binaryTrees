from Card import *
from DLLCards import CardsDouLiLi

deck = CardsDouLiLi()

suitKey = 0
while suitKey < (len(suit)):
    rankKey = 2
    while rankKey <= (len(rank) + 1):
        newCard = Cards(suit[suitKey], rank[rankKey])
        deck.push_back(newCard.suit, newCard.rank)
        rankKey += 1
    suitKey += 1

