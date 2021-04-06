class BST:
    
    class Node:

        def __init__(self, data):
            # Initialize node.
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        #Initialize empty BST.
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert_(data, self.root)

    def _insert_(self, data, node):
        # Will look for a place to insert a node with data.
        if data != node.data:
            if data < node.data:
                # The data belongs on the left side.
                if node.left is None:
                    node.left = BST.Node(data)
                else:
                    # Call _insert_ recursively on the left sub-tree.
                    self._insert_(data, node.left)
            else:
                # The data belongs on the right side.
                if node.right is None:
                    node.right = BST.Node(data)
                else:
                    # Call _insert_ recursively on the right sub-tree.
                    self._insert_(data, node.right)

#########################################
# HERE IS THE SOLUTION TO THE BST PROBLEM
#########################################
def min_value(root):
    if root is None:
        return -1
    current = bst.root
  
    # loop down to find the lefT most leaf.
    while current.left is not None:
        current = current.left
  
    return current.data
#########################################
# END OF SOLUTION
#########################################

bst = BST()

bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(10)

print("This is the smallest value in the BST: {}".format(min_value(bst)))