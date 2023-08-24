class Node:
    def __init__(self, data=None, next_node = None):
        self.data = data
        self.next_node = next_node
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        iterator = self.head
        while iterator:
            iterator = iterator.next
