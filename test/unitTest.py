import unittest
from CreateLinkList import deck
from CardsNode import NodeForCards
from DLLCards import CardsDouLiLi


class TestCards(unittest.TestCase):

    def test_push_an_element_into_the_list(self):
        self.assertEqual(deck.push_back("diamond", "10").suit, "diamond")
        self.assertEqual(deck.push_back("diamond", "10").rank, "10")

    def test_insert_after(self):
        self.assertEqual(deck.insert_after("123", "test", u"\u2665", "10").suit, "123")
        self.assertEqual(deck.insert_after("123", "test", u"\u2665", "A").rank, "test")

    def test_reverse(self):
        deck.reverse()
        self.assertEqual(deck.tail.rank,  "10")


if __name__ == '__main__':
    unittest.main()
