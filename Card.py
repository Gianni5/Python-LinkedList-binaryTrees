class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


rank = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
}
suit = {
    3: u"\u2665",  # Hearts
    2: u"\u2666",  # Diamonds
    1: u"\u2663",  # Clubs
    0: u"\u2660",  # Spades
}


