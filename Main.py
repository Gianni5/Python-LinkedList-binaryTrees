from DLLCards import CardsDouLiLi
from CardsNode import NodeForCards
from CreateLinkList import deck

'''
def main():
    main_cards = CardsDouLiLi()
    main_cards.head = NodeForCards("Diamonds", "J")
    e2 = NodeForCards("Diamonds", "10")
    e3 = NodeForCards("Diamonds", "9")
    main_cards.head.next = e2
    e2.next = e3
    main_cards.initiated()

    print("-" * 90)
    print("ADDING AT THE END")

    main_cards.push_back("Diamonds", "J")
    main_cards.push_back("Hearts", "K")
    main_cards.push_back("Clubs", "Q")
    main_cards.push_back("Spades", "A")
    main_cards.initiated()

    print("-" * 90)
    print("INSERTING AFTER CHOSEN NODE")

    main_cards.head = NodeForCards("Diamonds", "A")
    e2 = NodeForCards("Diamonds", "10")
    e3 = NodeForCards("Diamonds", "9")
    e4 = NodeForCards("Clubs", "7")
    e5 = NodeForCards("Hearts", "Q")
    main_cards.head.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    main_cards.insert_after(e4, "Spades", "5")
    main_cards.initiated()

    print("-" * 90)
    print("DELETING THE LAST NODE")

    main_cards.delete_at_end()
    main_cards.initiated()

    print("-" * 90)
    print(" DISPLAYING BY TRAVERSING BACKWARDS ")

    main_cards.display()
'''

'''
def main():
    main_cardsD = CardsDouLiLi()

    print("\n" + "DIAMOND ", "-" * 80)
    main_cardsD.push_back("Diamonds", "A")
    main_cardsD.push_back("Diamonds", "2")
    main_cardsD.push_back("Diamonds", "3")
    main_cardsD.push_back("Diamonds", "4")
    main_cardsD.push_back("Diamonds", "5")
    main_cardsD.push_back("Diamonds", "6")
    main_cardsD.push_back("Diamonds", "7")
    main_cardsD.push_back("Diamonds", "8")
    main_cardsD.push_back("Diamonds", "9")
    main_cardsD.push_back("Diamonds", "10")
    main_cardsD.push_back("Diamonds", "J")
    main_cardsD.push_back("Diamonds", "Q")
    main_cardsD.push_back("Diamonds", "K")

    main_cardsD.initiated()
    main_cardsD.delete_at_end()
    main_cardsD.initiated()

    print("\n" + "HEART ", "-" * 80)

    main_cardsH = CardsDouLiLi()
    main_cardsH.push_back("Hearts", "A")
    main_cardsH.push_back("Hearts", "2")
    main_cardsH.push_back("Hearts", "3")
    main_cardsH.push_back("Hearts", "4")
    main_cardsH.push_back("Hearts", "5")
    main_cardsH.push_back("Hearts", "6")
    main_cardsH.push_back("Hearts", "7")
    main_cardsH.push_back("Hearts", "8")
    main_cardsH.push_back("Hearts", "9")
    main_cardsH.push_back("Hearts", "10")
    main_cardsH.push_back("Hearts", "J")
    main_cardsH.push_back("Hearts", "Q")
    main_cardsH.push_back("Hearts", "K")

    main_cardsH.initiated()
    main_cardsH.delete_at_end()
    main_cardsH.initiated()

    print("\n" + "SPADE ", "-" * 80)

    main_cardsS = CardsDouLiLi()
    main_cardsS.push_back("Spades", "A")
    main_cardsS.push_back("Spades", "2")
    main_cardsS.push_back("Spades", "3")
    main_cardsS.push_back("Spades", "4")
    main_cardsS.push_back("Spades", "5")
    main_cardsS.push_back("Spades", "6")
    main_cardsS.push_back("Spades", "7")
    main_cardsS.push_back("Spades", "8")
    main_cardsS.push_back("Spades", "9")
    main_cardsS.push_back("Spades", "10")
    main_cardsS.push_back("Spades", "J")
    main_cardsS.push_back("Spades", "Q")
    main_cardsS.push_back("Spades", "K")

    main_cardsS.display()
    main_cardsS.delete_at_end()
    main_cardsS.initiated()

    print("\n" + "CLUB ", "-" * 80)
    main_cardsC = CardsDouLiLi()
    main_cardsC.push_back("Clubs", "A")
    main_cardsC.push_back("Clubs", "2")
    main_cardsC.push_back("Clubs", "3")
    main_cardsC.push_back("Clubs", "4")
    main_cardsC.push_back("Clubs", "5")
    main_cardsC.push_back("Clubs", "6")
    main_cardsC.push_back("Clubs", "7")
    main_cardsC.push_back("Clubs", "8")
    main_cardsC.push_back("Clubs", "9")
    main_cardsC.push_back("Clubs", "10")
    main_cardsC.push_back("Clubs", "J")
    main_cardsC.push_back("Clubs", "Q")
    main_cardsC.push_back("Clubs", "K")

    main_cardsC.initiated()
    main_cardsC.delete_at_end()
    main_cardsC.initiated()
'''

if __name__ == '__main__':

    deck.reverse()
    deck.display()
    print("*" * 30, "COMPLETED DECK")
    deck.delete_at_end()
    deck.display()
    print("*" * 35, "AFTER DELETE")

    deck.display()
    print("*" * 30)
    deck.insert_after("-" * 30, " INSERTING AFTER ", u"\u2665", "10")
    deck.display()
    print("*" * 30)


