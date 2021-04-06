# LINKED LIST SOLUTION HERE
class Linked_list:

    class Node:

        def __init__(self, data):
            # Initialize the node.
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        # Initialize empty linked list.
        self.head = None
        self.tail = None
#################################################
# HERE IS THE SOLUTION TO THE LINKED LIST PROBLEM
#################################################
    def insert_head(self, value):
        # Create a new node.
        new_node = Linked_list.Node(value)
        
        # If list is empty, point both head and tail to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # If list is not empty, only head will change.
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

#################################################
# END OF SOLUTION
#################################################

    def insert_tail(self, value):
        # Insert a new node at the back of the linked list.
        new_node = Linked_list.Node(value)
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node 