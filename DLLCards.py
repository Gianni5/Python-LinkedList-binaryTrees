import Card
import CardsNode
from CardsNode import NodeForCards


# Creating a doubly linked list class
class CardsDouLiLi:
    def __init__(self):
        self.head = None  # Initially there are no elements in the list
        self.tail = None
        self.count = 0

    def display(self):  # displaying the doubly linked list
        data = self.head
        while data is not None:
            self.count += 1
            print(data.suit, data.rank)
            data = data.next

    def push_back(self, newSuit, newRank):  # Adding an element after the last element
        new_node = NodeForCards(newSuit, newRank)
        new_node.prev = self.tail

        if self.tail == None:  # checks whether the list is empty, if so make both head and tail as new node
            self.head = new_node
            self.tail = new_node
            new_node.next = None  # the first element's previous pointer has to refer to null

        else:  # If list is not empty, change pointers accordingly
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node  # Make new node the new tail
        self.count += 1
        return new_node

    def insert_after(self, newSuit, newRank, afterSuit, afterRank):  # Inserting a new node after a given node
        new_node = NodeForCards(newSuit, newRank)
        selected_node = NodeForCards(afterSuit, afterRank)
        current_node = self.head
        while current_node is not None:
            if selected_node.suit == current_node.suit and selected_node.rank == current_node.rank:  # inserting after
                temp_node = current_node.next
                if temp_node is None:
                    current_node.next = new_node
                    self.tail = new_node
                    new_node.prev = current_node
                else:
                    current_node.next = new_node
                    new_node.prev = current_node
                    new_node.next = temp_node
                    temp_node.prev = new_node
                break

            current_node = current_node.next
        return new_node

    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    # Traversing backwards and Displaying each element of the list
    def reverse(self):
        data = self.tail
        while data is not None:
            print(data.suit, data.rank)
            data = data.prev
        return data


