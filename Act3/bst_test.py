from binarysearchtree import BinarySearchTree

# Create a binary search tree
bst = BinarySearchTree()

# Insert some values
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(17)

# Search for values
print("Searching for 5:", bst.search(5))  # Should return True
print("Searching for 8:", bst.search(8))  # Should return False

# Delete a value
# bst.delete(10)

# Print the tree
bst.print_tree()

# Traverse and print the tree in ascending order
values = bst.traverse()
print("Values in ascending order:", values)
