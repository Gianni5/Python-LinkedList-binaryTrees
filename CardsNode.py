# Creating a node class
class NodeForCards:
    def __init__(self, suit, rank):
        self.suit = suit  # adding an element to the node
        self.rank = rank  # adding an element to the node
        self.next = None  # Initially this node will not be linked with any other node
        self.prev = None  # It will not be linked in either direction

    def suit(self):
        return self.suit, self.rank



